from dataclasses import dataclass

from src.core.order.values.status import OrderStatus


@dataclass
class UpdateOrderDTO:
    order_price: int | None = None
    order_status: OrderStatus | None = None

    def __post_init__(self):
        if self.order_status is not None:
            self.order_status = self.order_status.value
