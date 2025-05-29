from fastapi import APIRouter

from database import SessionFactory
from user.authentication import hash_password
from user.models import User
from user.request import UserSignUpRequest

router = APIRouter(tags=["User"])


# 회원가입 API
@router.post("/users/sign-up")
def user_sign_up_handler(body: UserSignUpRequest):
    # 1) 클라이언트로부터 데이터(username, password)를 넘겨 받는다.

    # 2) 데이터를 User 테이블에 저장한다.
    hashed_password = hash_password(plain_password=body.password)
    new_user = User(username=body.username, password=hashed_password)

    session = SessionFactory()
    session.add(new_user)  # DB에 저장 X
    session.commit()  # DB에 저장

    # 3) 응답을 반환한다.
    return {
        "id": new_user.id,
        "username": new_user.username,
        "password": new_user.password,
        "created_at": new_user.created_at,
    }
