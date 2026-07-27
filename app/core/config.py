from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "BlueWatch API"
    api_version: str = "1.0.0"
    debug: bool = True

    database_url: str
    secret_key: str
    groq_api_key: str          # <-- Add this

    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()