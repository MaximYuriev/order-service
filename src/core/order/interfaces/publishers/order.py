import uuid
from abc import ABC, abstractmethod


class IOrderPublisher(ABC):
    @abstractmethod
    async def prepare_order(self, user_id: uuid.UUID) -> None:
        pass
