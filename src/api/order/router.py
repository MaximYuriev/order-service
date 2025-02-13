import uuid

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter

from src.api.order.response import OrderResponse
from src.core.order.services.order import OrderService

order_router = APIRouter(prefix="/order", tags=["Order"])


@order_router.post("")
@inject
async def create_order(
        user_id: uuid.UUID,
        order_service: FromDishka[OrderService]
) -> OrderResponse:
    await order_service.create_order(user_id)
    return OrderResponse(detail="Заказ в скором времени будет оформлен!")
