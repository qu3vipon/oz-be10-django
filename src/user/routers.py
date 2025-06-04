from fastapi import APIRouter, HTTPException, Depends
from fastapi.requests import Request

from database import SessionFactory, get_session
from user.authentication import hash_password, check_password
from user.models import User
from user.request import UserSignUpRequest, UserLoginRequest

router = APIRouter(tags=["User"])


# 회원가입 API
@router.post("/users/sign-up")
def user_sign_up_handler(
    body: UserSignUpRequest,
    session = Depends(get_session),  # 의존성 주입(Dependency Injection)
):
    # 1) 클라이언트로부터 데이터(username, password)를 넘겨 받는다.

    # 2) 데이터를 User 테이블에 저장한다.
    hashed_password = hash_password(plain_password=body.password)
    new_user = User(username=body.username, password=hashed_password)

    session.add(new_user)  # DB에 저장 X
    session.commit()  # DB에 저장

    # 3) 응답을 반환한다.
    return {
        "id": new_user.id,
        "username": new_user.username,
        "password": new_user.password,
        "created_at": new_user.created_at,
    }

@router.post("/users/login")
def user_login_handler(
    request: Request,
    body: UserLoginRequest,
    session = Depends(get_session),
):
    # 1) 클라이언트로부터 데이터(username, password)를 넘겨 받음

    # 2) 사용자 정보(해시 값)를 username을 기준으로 조회
    if not (user := session.query(User).filter_by(username=body.username).first()):
        raise HTTPException(status_code=404, detail="User not found")

    # 3) password <-> 해시 값 비교
    if not check_password(
        plain_password=body.password,  # 1)에서 클라이어가 넘기 비밀번호
        hashed_password=user.password,  # 2)에서 DB에서 가져온 해시 값
    ):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # 4) 결과 응답
    # 로그인 유지되는 동안 서버에서 사용하고 싶은 클라이언트 정보
    request.session["user_id"] = user.id
    request.session["username"] = user.username
    return {"id": user.id, "username": user.username}


@router.post("/users/logout")
def user_logout_handler(request: Request):
    request.session.clear()
    return {"message": "Logged out"}


@router.get("/users/me")
def user_me_handler(request: Request):
    user_id = request.session.get("user_id")
    username = request.session.get("username")

    if user_id and username:
        return {"id": user_id, "username": username}

    raise HTTPException(status_code=401, detail="Session Not Found")
