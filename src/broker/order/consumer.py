from faststream.rabbit import RabbitRouter

from src.broker.order.schemas import CanceledOrderSchema

rmq_order_router = RabbitRouter(prefix="order-")

@rmq_order_router.subscriber("cancel", exchange="order")
async def cancel_order(
        canceled_order_schema: CanceledOrderSchema,

) -> None:
    ...
