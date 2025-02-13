import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.order.dto.order import UpdateOrderDTO
from src.core.order.entities.order import Order
from src.core.order.exceptions.order import OrderNotFoundException
from src.core.order.interfaces.repositories.order import IOrderRepository
from src.core.order.models.order import OrderModel


class OrderRepository(IOrderRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save_order_on_db(self, order: Order) -> None:
        order_model = OrderModel.from_entity(order)
        self._session.add(order_model)
        await self._session.commit()

    async def get_order_from_db(self, order_id: uuid.UUID) -> Order:
        order_model = await self._get_order_model(order_id)
        return order_model.to_entity()

    async def update_order_on_db(self, order_id: uuid.UUID, update_order: UpdateOrderDTO) -> None:
        order_model = await self._get_order_model(order_id)
        update_order_data = update_order.__dict__
        for key, value in update_order_data.items():
            setattr(order_model, key, value)
        await self._session.commit()

    async def _get_order_model(self, order_id: uuid.UUID, **kwargs) -> OrderModel:
        query = (
            select(OrderModel)
            .where(OrderModel.order_id == order_id)
            .filter_by(**kwargs)
        )
        order_model = await self._session.scalar(query)
        if order_model is None:
            raise OrderNotFoundException(order_id=order_id)
        return order_model
