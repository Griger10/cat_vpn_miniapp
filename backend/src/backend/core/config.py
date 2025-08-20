from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")
    host: str
    port: int
    user: str
    password: SecretStr
    db: str

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}"
            f"@{self.host}:{self.port}/{self.db}"
        )


class BotConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BOT_")
    token: SecretStr
    admin_ids: str
    admin_url: str
    web_app_url: str


class RedisConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="REDIS_")
    host: str
    port: int


class Config(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)
    postgres_config: PostgresConfig = PostgresConfig()
    bot_config: BotConfig = BotConfig()
    redis_config: RedisConfig = RedisConfig()
