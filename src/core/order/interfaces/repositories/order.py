import uuid
from abc import ABC, abstractmethod

from src.core.order.dto.order import UpdateOrderDTO
from src.core.order.entities.order import Order, CanceledOrder


class IOrderRepository(ABC):
    @abstractmethod
    async def save_order_on_db(self, order: Order) -> None:
        pass

    @abstractmethod
    async def get_order_from_db(self, order_id: uuid.UUID) -> Order:
        pass

    @abstractmethod
    async def update_order_on_db(self, order_id: uuid.UUID, update_order: UpdateOrderDTO) -> None:
        pass


class ICanceledOrderRepository(ABC):
    @abstractmethod
    async def save_canceled_order_on_db(self, canceled_order: CanceledOrder) -> None:
        pass
