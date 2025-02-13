import uuid
from dataclasses import dataclass

from src.core.commons.exceptions import ApplicationException


class OrderException(ApplicationException):
    @property
    def message(self) -> str:
        return "Ошибка сервиса заказов!"


@dataclass
class OrderNotFoundException(OrderException):
    order_id: uuid.UUID

    @property
    def message(self) -> str:
        return f"Заказ с id={self.order_id !r} не найден!"
