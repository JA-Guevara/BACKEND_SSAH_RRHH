class AuthError(Exception):
    """Base exception for auth domain errors."""


class UserAlreadyExistsError(AuthError):
    pass


class InvalidCredentialsError(AuthError):
    pass


class TokenExpiredError(AuthError):
    pass
