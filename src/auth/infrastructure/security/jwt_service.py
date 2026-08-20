from datetime import UTC, datetime, timedelta
from hashlib import sha256
from uuid import uuid4

from jose import ExpiredSignatureError, JWTError, jwt
from src.auth.domain.exceptions import InvalidTokenError, TokenExpiredError
from src.auth.ports.outgoing.token_service import TokenService
from src.config.settings import settings


class JWTService(TokenService):
    def create_access_token(self, subject: str) -> str:
        expires_delta = timedelta(minutes=settings.app_access_token_expire_minutes)
        now = datetime.now(UTC)
        to_encode = {
            "sub": subject,
            "type": "access",
            "jti": str(uuid4()),
            "iat": now,
            "exp": now + expires_delta,
        }
        return jwt.encode(to_encode, settings.app_secret_key, algorithm=settings.app_algorithm)

    def create_refresh_token(self, subject: str) -> tuple[str, str, datetime]:
        expires_delta = timedelta(days=settings.app_refresh_token_expire_days)
        now = datetime.now(UTC)
        expires_at = now + expires_delta
        token_id = str(uuid4())
        to_encode = {
            "sub": subject,
            "type": "refresh",
            "jti": token_id,
            "iat": now,
            "exp": expires_at,
        }
        token = jwt.encode(to_encode, settings.app_secret_key, algorithm=settings.app_algorithm)
        return token, token_id, expires_at

    def decode_token(self, token: str, expected_type: str) -> dict[str, object]:
        try:
            payload = jwt.decode(
                token,
                settings.app_secret_key,
                algorithms=[settings.app_algorithm],
            )
        except ExpiredSignatureError as exc:
            raise TokenExpiredError("El token expiró") from exc
        except JWTError as exc:
            raise InvalidTokenError("Token inválido") from exc

        if payload.get("type") != expected_type or not payload.get("sub"):
            raise InvalidTokenError("El tipo de token no es válido")
        return payload

    def fingerprint(self, token: str) -> str:
        return sha256(token.encode("utf-8")).hexdigest()
