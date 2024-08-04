from dotenv import load_dotenv  # type: ignore
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore


load_dotenv()


class Settings(BaseSettings):
    API_KEY: str
    ON_SITE: bool

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore[call-arg]
