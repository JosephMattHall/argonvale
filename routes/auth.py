from sanic import Blueprint, response
from database import SessionLocal
from models import User
import hashlib

bp = Blueprint("auth", url_prefix="/auth")

@bp.route("/register", methods=["POST"])
async def register(request):
    data = request.json
    db = SessionLocal()
    existing_user = db.query(User).filter_by(username=data["username"]).first()
    if existing_user:
        db.close()
        return response.json({"error": "User already exists"}, status=400)

    hashed_password = hashlib.sha256(data["password"].encode()).hexdigest()
    user = User(username=data["username"], password=hashed_password)
    db.add(user)
    db.commit()
    db.close()

    return response.json({"message": "User registered successfully"}, status=201)

@bp.route("/login", methods=["POST"])
async def login(request):
    data = request.json
    db = SessionLocal()
    user = db.query(User).filter_by(username=data["username"]).first()
    if not user:
        db.close()
        return response.json({"error": "Invalid credentials"}, status=401)

    hashed_password = hashlib.sha256(data["password"].encode()).hexdigest()
    if user.password != hashed_password:
        db.close()
        return response.json({"error": "Invalid credentials"}, status=401)

    # You can include JWT token generation here

    db.close()
    return response.json({"message": "Login successful"})
