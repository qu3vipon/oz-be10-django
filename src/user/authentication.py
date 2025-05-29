import bcrypt

# encode: str -> bytes
# decode: bytes -> str
def hash_password(plain_password: str) -> str:
    hash_bytes: bytes = bcrypt.hashpw(
        plain_password.encode("utf-8"), bcrypt.gensalt()
    )
    return hash_bytes.decode("utf-8")
