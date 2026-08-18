class RefreshToken:
    def __init__(self, token_service):
        self.token_service = token_service

    def execute(self, refresh_token: str):
        payload = self.token_service.decode_token(refresh_token)
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("Token inválido")

        return {
            "access_token": self.token_service.create_access_token(user_id),
            "refresh_token": self.token_service.create_refresh_token(user_id),
            "token_type": "bearer",
        }
