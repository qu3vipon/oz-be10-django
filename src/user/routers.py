from fastapi import APIRouter

router = APIRouter(tags=["User"])


@router.get("/users")
def get_users_handler():
    return [
        {"id": 1, "username": "Alice"},
        {"id": 2, "username": "Bob"},
        {"id": 3, "username": "Charlie"},
    ]
