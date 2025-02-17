from typing import AsyncIterable

from dishka import Provider, from_context, Scope, provide
from faststream.rabbit import RabbitBroker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession

from src.broker.order.adapter import ConsumerOrderAdapter
from src.config import Config
from src.core.order.interfaces.publishers.order import IOrderPublisher
from src.core.order.interfaces.uow.order import IOrderUoW
from src.core.order.publishers.order import RMQOrderPublisher
from src.core.order.services.order import OrderService
from src.core.order.uow.order import OrderUoW


class SQLAlchemyProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_async_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.postgres.db_url, echo=False)

    @provide(scope=Scope.APP)
    def get_async_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session


class RMQProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.REQUEST)
    async def get_broker_connection(self, config: Config) -> AsyncIterable[RabbitBroker]:
        async with RabbitBroker(config.rmq.rmq_url) as broker:
            yield broker


class OrderProvider(Provider):
    scope = Scope.REQUEST

    order_uow = provide(OrderUoW, provides=IOrderUoW)
    order_publisher = provide(RMQOrderPublisher, provides=IOrderPublisher)
    order_service = provide(OrderService)


class ConsumerOrderProvider(Provider):
    scope = Scope.REQUEST

    consumer_order_adapter = provide(ConsumerOrderAdapter)
