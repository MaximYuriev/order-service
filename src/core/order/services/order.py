import uuid

from src.core.order.dto.order import UpdateOrderDTO
from src.core.order.entities.order import Order, CanceledOrder
from src.core.order.interfaces.publishers.order import IOrderPublisher
from src.core.order.interfaces.uow.order import IOrderUoW
from src.core.order.values.status import OrderStatus


class OrderService:
    def __init__(self, uow: IOrderUoW, publisher: IOrderPublisher):
        self._uow = uow
        self._publisher = publisher

    async def create_order(self, user_id: uuid.UUID) -> None:
        async with self._uow:
            order = Order(
                user_id=user_id,
                order_status=OrderStatus.PREPARE,
            )
            await self._publisher.prepare_order(order.order_id, user_id)
            await self._uow.order_repository.save_order_on_db(order)
            await self._uow.commit()

    async def cancel_order(self, order_id: uuid.UUID, reason: str | None = None) -> None:
        async with self._uow:
            update_order_data = UpdateOrderDTO(
                order_status=OrderStatus.CANCEL,
            )
            canceled_order = CanceledOrder(
                order_id=order_id,
                reason=reason
            )
            await self._uow.order_repository.update_order_on_db(
                order_id=order_id,
                update_order=update_order_data,
            )
            await self._uow.canceled_order_repository.save_canceled_order_on_db(canceled_order=canceled_order)
            await self._uow.commit()
