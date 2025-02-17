from sqlalchemy.ext.asyncio import AsyncSession

from src.core.order.entities.order import CanceledOrder
from src.core.order.interfaces.repositories.order import ICanceledOrderRepository
from src.core.order.models.order import CanceledOrderModel


class CanceledOrderRepository(ICanceledOrderRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save_canceled_order_on_db(self, canceled_order: CanceledOrder) -> None:
        canceled_order_model = CanceledOrderModel.from_entity(canceled_order)
        self._session.add(canceled_order_model)
