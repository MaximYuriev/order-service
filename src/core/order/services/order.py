import uuid

from src.core.order.entities.order import Order
from src.core.order.interfaces.repository import IOrderRepository
from src.core.order.values.status import OrderStatus


class OrderServices:
    def __init__(self, repository: IOrderRepository):
        self._repository = repository

    async def create_order(self, user_id: uuid.UUID) -> None:
        order = Order(
            user_id=user_id,
            order_status=OrderStatus.PREPARE,
        )
        # сделать отправку в сервис basket
        await self._repository.save_order_on_db(order)
