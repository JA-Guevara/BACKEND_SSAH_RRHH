class RegisterUser:
    def __init__(self, user_repository, password_hasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, name: str, email: str, password: str):
        if self.user_repository.get_by_email(email):
            raise ValueError("El usuario ya existe")

        hashed_password = self.password_hasher.hash(password)
        user = self.user_repository.create({
            "name": name,
            "email": email,
            "hashed_password": hashed_password,
        })
        return user
