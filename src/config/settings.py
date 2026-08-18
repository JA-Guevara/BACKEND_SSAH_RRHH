from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    app_debug: bool = True
    app_secret_key: str = "change-me-in-production"
    app_algorithm: str = "HS256"
    app_access_token_expire_minutes: int = 60
    app_refresh_token_expire_days: int = 7
    database_url: str = "postgresql+psycopg://user:password@localhost:5432/app_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        case_sensitive=False,
    )


settings = Settings()
