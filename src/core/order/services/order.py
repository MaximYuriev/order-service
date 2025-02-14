import uuid

from src.core.order.entities.order import Order
from src.core.order.interfaces.publishers.order import IOrderPublisher
from src.core.order.interfaces.repositories.order import IOrderRepository
from src.core.order.values.status import OrderStatus


class OrderService:
    def __init__(self, repository: IOrderRepository, publisher: IOrderPublisher):
        self._repository = repository
        self._publisher = publisher

    async def create_order(self, user_id: uuid.UUID) -> None:
        order = Order(
            user_id=user_id,
            order_status=OrderStatus.PREPARE,
        )
        await self._publisher.prepare_order(order.order_id, user_id)
        await self._repository.save_order_on_db(order)
