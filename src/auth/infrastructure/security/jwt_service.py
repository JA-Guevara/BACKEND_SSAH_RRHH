from datetime import datetime, timedelta

from jose import JWTError, jwt

from src.config.settings import settings


class JWTService:
    def create_access_token(self, subject: str) -> str:
        expires_delta = timedelta(minutes=settings.app_access_token_expire_minutes)
        expire = datetime.utcnow() + expires_delta
        to_encode = {"sub": subject, "exp": expire}
        return jwt.encode(to_encode, settings.app_secret_key, algorithm=settings.app_algorithm)

    def create_refresh_token(self, subject: str) -> str:
        expires_delta = timedelta(days=settings.app_refresh_token_expire_days)
        expire = datetime.utcnow() + expires_delta
        to_encode = {"sub": subject, "exp": expire}
        return jwt.encode(to_encode, settings.app_secret_key, algorithm=settings.app_algorithm)

    def decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, settings.app_secret_key, algorithms=[settings.app_algorithm])
        except JWTError as exc:  # pragma: no cover
            raise ValueError("Token inválido") from exc
