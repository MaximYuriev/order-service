from sqlalchemy.ext.asyncio import AsyncSession

from src.core.order.interfaces.repositories.order import IOrderRepository, ICanceledOrderRepository
from src.core.order.interfaces.uow.order import IOrderUoW
from src.core.order.repositories.canceled_order import CanceledOrderRepository
from src.core.order.repositories.order import OrderRepository


class OrderUoW(IOrderUoW):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def __aenter__(self) -> None:
        self._order_repository = OrderRepository(self._session)
        self._canceled_order_repository = CanceledOrderRepository(self._session)

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.rollback()
        await self._session.close()

    @property
    def order_repository(self) -> IOrderRepository:
        return self._order_repository

    @property
    def canceled_order_repository(self) -> ICanceledOrderRepository:
        return self._canceled_order_repository

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
