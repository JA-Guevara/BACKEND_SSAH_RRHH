class LogoutUser:
    def execute(self, token: str):
        return {"message": "Sesión cerrada", "token": token}
