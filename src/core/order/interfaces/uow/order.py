from abc import ABC, abstractmethod

from src.core.order.interfaces.repositories.order import IOrderRepository, ICanceledOrderRepository


class IOrderUoW(ABC):
    @property
    @abstractmethod
    def order_repository(self) -> IOrderRepository:
        ...

    @property
    @abstractmethod
    def canceled_order_repository(self) -> ICanceledOrderRepository:
        ...

    @abstractmethod
    async def __aenter__(self) -> None:
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def rollback(self) -> None:
        ...
