import bcrypt

# encode: str -> bytes
# decode: bytes -> str
def hash_password(plain_password: str) -> str:
    hash_bytes: bytes = bcrypt.hashpw(
        plain_password.encode("utf-8"), bcrypt.gensalt()
    )
    return hash_bytes.decode("utf-8")


def check_password(plain_password: str, hashed_password: str) -> bool:
    # plain_password -> 사용자가 로그인시 입력한 평문 암호
    # hashed_password -> 회원가입시 데이터베이스 저장된 해시 값
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
