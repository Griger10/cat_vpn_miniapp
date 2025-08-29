from collections.abc import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from cat_vpn_miniapp.bootstrap.config import Config


class DatabaseProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, config: Config) -> AsyncIterable[AsyncEngine]:
        engine = create_async_engine(config.postgres_config.database_url)
        yield engine
        await engine.dispose(True)

    @provide
    async def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, pool: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with pool() as session:
            yield session
