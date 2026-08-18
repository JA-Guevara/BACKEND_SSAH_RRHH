from passlib.context import CryptContext

from src.auth.ports.outgoing.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    def __init__(self):
        self._context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash(self, password: str) -> str:
        return self._context.hash(password)

    def verify(self, password: str, hashed_password: str) -> bool:
        return self._context.verify(password, hashed_password)
