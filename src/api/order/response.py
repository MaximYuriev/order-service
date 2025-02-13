from src.api.commons.response import BaseResponse
from src.api.order.schemas.order import OrderSchema


class OrderResponse(BaseResponse):
    data: OrderSchema | None = None
