import uuid

from pydantic import BaseModel

from src.api.order.schemas.product_on_order import ProductOnOrderSchema
from src.core.order.values.status import OrderStatus


class OrderSchema(BaseModel):
    order_id: uuid.UUID
    user_id: uuid.UUID
    order_price: int | None = None
    order_status: OrderStatus

    product_list: list[ProductOnOrderSchema]
