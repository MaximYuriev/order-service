from dataclasses import dataclass

from src.core.order.values.status import OrderStatus


@dataclass
class UpdateOrderDTO:
    order_price: int | None = None
    order_status: OrderStatus | None = None
