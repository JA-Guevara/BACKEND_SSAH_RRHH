import bcrypt
from src.auth.domain.exceptions import InvalidPasswordError
from src.auth.ports.outgoing.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    def hash(self, password: str) -> str:
        password_bytes = password.encode("utf-8")
        if len(password_bytes) > 72:
            raise InvalidPasswordError("La contraseña no puede superar 72 bytes")
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

    def verify(self, password: str, hashed_password: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
        except (ValueError, TypeError):
            return False
