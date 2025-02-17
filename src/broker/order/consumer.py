from dishka.integrations.faststream import inject, FromDishka
from faststream.rabbit import RabbitRouter

from src.broker.order.adapter import ConsumerOrderAdapter
from src.broker.order.schemas import CanceledOrderSchema

rmq_order_router = RabbitRouter(prefix="order-")


@rmq_order_router.subscriber("cancel", exchange="order")
@inject
async def cancel_order(
        canceled_order_schema: CanceledOrderSchema,
        consumer_order_adapter: FromDishka[ConsumerOrderAdapter],
) -> None:
    await consumer_order_adapter.cancel_order(canceled_order_schema)
