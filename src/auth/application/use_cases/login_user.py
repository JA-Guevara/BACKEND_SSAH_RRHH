class LoginUser:
    def __init__(self, user_repository, password_hasher, token_service):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_service = token_service

    def execute(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if not user or not self.password_hasher.verify(password, user.hashed_password):
            raise ValueError("Credenciales inválidas")

        access_token = self.token_service.create_access_token(str(user.id))
        refresh_token = self.token_service.create_refresh_token(str(user.id))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
