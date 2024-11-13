from fasthtml import APIRouter
from app.services.firebase import add_marker, get_markers, update_marker, delete_marker

router = APIRouter()

@router.post("/markers")
async def create_marker(marker_data: dict, request: Request):
    if not request.state.user:
        return {"error": "Unauthorized"}, 401
    # Opcional: puedes vincular el marcador al user_id del usuario
    marker_data["user_id"] = request.state.user["uid"]
    return add_marker(marker_data)

@router.get("/markers")
async def read_markers():
    return get_markers()

@router.put("/markers/{marker_id}")
async def modify_marker(marker_id: str, marker_data: dict):
    return update_marker(marker_id, marker_data)

@router.delete("/markers/{marker_id}")
async def remove_marker(marker_id: str):
    return delete_marker(marker_id)


