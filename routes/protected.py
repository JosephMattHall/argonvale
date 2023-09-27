from sanic import Blueprint, response
from utils import get_user_id_from_token
from database import SessionLocal
from models import User

bp = Blueprint("protected", url_prefix="/protected")

@bp.route("/route1", methods=["GET"])
async def protected_route_1(request):
    auth_header = request.headers.get("Authorization")
    user_id = get_user_id_from_token(auth_header)
    if not user_id:
        return response.json({"error": "Unauthorized"}, status=401)

    # You can perform additional authorization checks if needed
    # For example, check if the user has certain permissions

    return response.json({"message": "Protected route 1 accessed successfully"})

@bp.route("/route2", methods=["GET"])
async def protected_route_2(request):
    auth_header = request.headers.get("Authorization")
    user_id = get_user_id_from_token(auth_header)
    if not user_id:
        return response.json({"error": "Unauthorized"}, status=401)

    # You can perform additional authorization checks if needed
    # For example, check if the user has certain permissions

    return response.json({"message": "Protected route 2 accessed successfully"})

# Other protected route handlers can be added here
