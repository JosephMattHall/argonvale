from sanic import Blueprint, response
from database import SessionLocal
from models import Companion


bp = Blueprint("companion", url_prefix="/companion")

@bp.route("/create", methods=["POST"])
async def create_companion(request):
    data = request.json
    db = SessionLocal()
    existing_companion = db.query(Companion).filter_by(name=data["name"]).first()
    if existing_companion:
        db.close()
        return response.json({"error": "Companion name already exists"}, status=400)

    companion = Companion(
        user_id=data["user_id"],
        name=data["name"],
        level=1,
        strength=5,
        defense=5,
        speed=5,
        HP=10,
        image=data["image"],
        type=data["type"]
    )

    db.add(companion)
    db.commit()
    db.close()

    return response.json({"message": "Companion created successfully"}, status=201)

# Other companion-related route handlers can be added here
