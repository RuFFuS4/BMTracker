from fasthtml import Request, HTTPException
from app.services.firebase import verify_user_token

async def auth_middleware(request: Request, call_next):
    id_token = request.headers.get("Authorization")
    if id_token:
        user_data = verify_user_token(id_token)
        if user_data:
            request.state.user = user_data
            return await call_next(request)
    raise HTTPException(status_code=401, detail="Unauthorized")
