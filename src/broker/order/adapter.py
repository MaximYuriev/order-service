from src.broker.order.schemas import CanceledOrderSchema
from src.core.order.services.order import OrderService


class ConsumerOrderAdapter:
    def __init__(self, service: OrderService):
        self._service = service

    async def cancel_order(self, cancel_order_schema: CanceledOrderSchema) -> None:
        canceled_order_data = cancel_order_schema.model_dump()
        await self._service.cancel_order(**canceled_order_data)
