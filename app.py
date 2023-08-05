import datetime
import os
from hashlib import sha256
import jwt
from sanic import Sanic, response
import motor.motor_asyncio
from dotenv import load_dotenv
from bson.objectid import ObjectId
import secrets

load_dotenv()

MONGODB_HOST = os.getenv("MONGODB_HOST")
MONGODB_PORT = int(os.getenv("MONGODB_PORT"))
MONGODB_DBNAME = os.getenv("MONGODB_DBNAME")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Sanic("myapp")
db = None

salt = secrets.token_bytes(32)

"""
TODO: salt password

salted_password = salt + password.encode()
hashed_password = sha256(salted_password).hexdigest()


"""

# Models

class Companion:
    def __init__(self, user_id, name, level, strength, defense, speed, HP, image, type):
        self.user_id = user_id
        self.name = name
        self.level = level
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.HP = HP
        self.image = image
        self.type = type


# Functions 

# Helper function to extract user_id from the Authorization token
def get_user_id_from_token(authorization_header):
    if not authorization_header or not authorization_header.startswith("Bearer "):
        return None

    token = authorization_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

async def create_companion(data, user_id):
    companion = Companion(
        user_id=user_id,
        name=data["name"],
        level=1,
        strength=5,
        defense=5,
        speed=5,
        HP=10,
        image=data["image"],
        type=data["type"]
    )
    await db.companions.insert_one(companion.__dict__)

async def create_user(data):
    hashed_password = sha256(data["password"].encode()).hexdigest()
    user = {
        "username": data["username"],
        "password": hashed_password,
    }
    await db.users.insert_one(user)


@app.route("/auth/register", methods=["POST"])
async def register(request):
    data = request.json
    existing_user = await db.users.find_one({"username": data["username"]})
    if existing_user:
        return response.json({"error": "User already exists"}, status=400)

    await create_user(data)
    return response.json({"message": "User registered successfully"}, status=201)


@app.route("/auth/login", methods=["POST"])
async def login(request):
    data = request.json
    user = await db.users.find_one({"username": data["username"]})
    if not user:
        return response.json({"error": "Invalid credentials"}, status=401)

    hashed_password = sha256(data["password"].encode()).hexdigest()
    if user["password"] != hashed_password:
        return response.json({"error": "Invalid credentials"}, status=401)

    payload = {"user_id": str(user["_id"]), "username": user["username"]}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return response.json({"access_token": token})


@app.route("/companion/create", methods=["POST"])
async def create_companion_route(request):
    data = request.json

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return response.json({"error": "Unauthorized"}, status=401)

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return response.json({"error": "Token has expired"}, status=401)
    except jwt.InvalidTokenError:
        return response.json({"error": "Invalid token"}, status=401)

    user_id = payload.get("user_id")
    if not user_id:
        return response.json({"error": "User ID not found in token"}, status=401)

    existing_companion = await db.companions.find_one({"name": data["name"]})
    if existing_companion:
        return response.json({"error": "Companion name already exists"}, status=400)

    await create_companion(data, user_id)
    return response.json({"message": "Companion created successfully"}, status=201)

@app.post("/companion/start_training/<companion_id>")
async def start_training_course(request, companion_id):
    # Get the user_id from the Authorization token
    auth_header = request.headers.get("Authorization")
    user_id = get_user_id_from_token(auth_header)
    if not user_id:
        return response.json({"error": "Unauthorized"}, status=401)

    # Check if the companion belongs to the user
    companion = await db.companions.find_one({"_id": ObjectId(companion_id), "user_id": user_id})
    if not companion:
        return response.json({"error": "Companion not found or does not belong to the user"}, status=404)

    # Check if the companion is already training
    if "training_end_time" in companion:
        return response.json({"error": "Companion is already undergoing training"}, status=400)

    # Calculate the training duration based on the companion's level
    training_duration = calculate_training_duration(companion["level"])

    # Calculate the training end time
    training_end_time = datetime.utcnow() + timedelta(seconds=training_duration)

    # Update the companion document with the training_end_time
    await db.companions.update_one({"_id": ObjectId(companion_id)}, {"$set": {"training_end_time": training_end_time}})

    return response.json({"message": "Training course started successfully", "end_time": training_end_time})


@app.put("/companion/finish_training/<companion_id>")
async def finish_training_course(request, companion_id):
    # Get the user_id from the Authorization token
    auth_header = request.headers.get("Authorization")
    user_id = get_user_id_from_token(auth_header)
    if not user_id:
        return response.json({"error": "Unauthorized"}, status=401)

    # Check if the companion belongs to the user
    companion = await db.companions.find_one({"_id": ObjectId(companion_id), "user_id": user_id})
    if not companion:
        return response.json({"error": "Companion not found or does not belong to the user"}, status=404)

    # Check if the companion is actually undergoing training
    if "training_end_time" not in companion:
        return response.json({"error": "Companion is not undergoing any training"}, status=400)

    # Check if the training course is finished
    if companion["training_end_time"] > datetime.utcnow():
        return response.json({"error": "Training course is not yet completed"}, status=400)

    # Reset the training_end_time and update the companion's document
    await db.companions.update_one({"_id": ObjectId(companion_id)}, {"$unset": {"training_end_time": 1}})

    # Apply any bonuses or rewards for completing the training course (if applicable)
    apply_training_bonuses(companion_id)

    return response.json({"message": "Training course finished successfully"})

@app.route("/companion/training_status", methods=["GET"])
async def training_status(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return response.json({"error": "Unauthorized"}, status=401)

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return response.json({"error": "Token has expired"}, status=401)
    except jwt.InvalidTokenError:
        return response.json({"error": "Invalid token"}, status=401)

    user_id = payload.get("user_id")
    if not user_id:
        return response.json({"error": "User ID not found in token"}, status=401)

    companions = await db.companions.find({"user_id": user_id}).to_list(None)

    training_status = {}
    for companion in companions:
        name = companion["name"]
        if "training_end_time" in companion:
            end_time = companion["training_end_time"]
            time_remaining = max((end_time - datetime.utcnow()).total_seconds(), 0)
            status = "training" if time_remaining > 0 else "finish"
            training_status[name] = {
                "status": status,
                "time_remaining": time_remaining
            }
        else:
            training_status[name] = {"status": "ready"}

    return response.json({"training_status": training_status})


@app.route("/protected-route", methods=["GET"])
async def protected_route(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return response.json({"error": "Unauthorized"}, status=401)

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return response.json({"error": "Token has expired"}, status=401)
    except jwt.InvalidTokenError:
        return response.json({"error": "Invalid token"}, status=401)

    return response.json({"message": "Protected route accessed successfully"})


@app.listener("before_server_start")
async def setup_app(app, loop):
    global db
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_HOST, MONGODB_PORT)
    db = client[MONGODB_DBNAME]
    await db.companions.create_index("name", unique=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
