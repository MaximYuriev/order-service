import uuid
from dataclasses import dataclass, field

from src.core.order.values.status import OrderStatus


@dataclass
class Order:
    order_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    user_id: uuid.UUID
    order_price: int | None = field(default=None, kw_only=True)
    order_status: OrderStatus

    def __post_init__(self):
        self.order_status = self.order_status.value
