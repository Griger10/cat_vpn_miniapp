from dishka import Provider, Scope, from_context, provide

from cat_vpn_miniapp.domain.config import Config


class ConfigProvider(Provider):
    scope = Scope.APP

    config = from_context(provides=Config, scope=Scope.APP)

    @provide
    async def get_bot_config(self, config: Config) -> Config:
        return config
