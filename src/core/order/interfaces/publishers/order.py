import uuid
from abc import ABC, abstractmethod


class IOrderPublisher(ABC):
    @abstractmethod
    async def prepare_order(self, order_id: uuid.UUID, user_id: uuid.UUID) -> None:
        pass
