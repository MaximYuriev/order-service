import uuid

from aio_pika import RobustExchange, RobustQueue
from faststream.rabbit import RabbitBroker, RabbitQueue, RabbitExchange

from src.core.order.interfaces.publishers.order import IOrderPublisher
from src.core.order.schemas.order import OrderBrokerSchema, PrepareOrderBrokerSchema


class RMQOrderPublisher(IOrderPublisher):
    _EXCHANGE_NAME = "order"
    _PREPARE_ORDER_QUEUE_NAME = "order-prepare"

    def __init__(self, broker: RabbitBroker):
        self._broker = broker

    async def prepare_order(self, order_id: uuid.UUID, user_id: uuid.UUID) -> None:
        exchange, queue = await self._prepare_to_publish(self._PREPARE_ORDER_QUEUE_NAME)
        order_schema = PrepareOrderBrokerSchema(order_id=order_id, user_id=user_id)
        await self._publish(exchange, queue, order_schema)

    async def _prepare_to_publish(self, queue_name: str) -> tuple[RobustExchange, RobustQueue]:
        exchange = await self._declare_exchange()
        queue = await self._declare_queue(queue_name)
        await self._bind_queue_to_exchange(exchange, queue)
        return exchange, queue

    async def _publish(
            self,
            exchange: RobustExchange,
            queue: RobustQueue,
            order_schema: OrderBrokerSchema,
    ) -> None:
        await self._broker.publish(
            message=order_schema,
            exchange=exchange.name,
            routing_key=queue.name,
        )

    async def _declare_exchange(self) -> RobustExchange:
        exchange = RabbitExchange(self._EXCHANGE_NAME)
        return await self._broker.declare_exchange(exchange)

    async def _declare_queue(self, queue_name: str) -> RobustQueue:
        rabbit_queue = RabbitQueue(queue_name)
        queue = await self._broker.declare_queue(rabbit_queue)
        return queue

    @staticmethod
    async def _bind_queue_to_exchange(exchange: RobustExchange, queue: RobustQueue) -> None:
        await queue.bind(
            exchange=exchange.name,
            routing_key=queue.name,
        )
