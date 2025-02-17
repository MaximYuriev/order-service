from dishka.integrations.faststream import setup_dishka
from faststream import FastStream
from faststream.rabbit import RabbitBroker

from src.broker.order.consumer import rmq_order_router
from src.main import config, container

broker = RabbitBroker(url=config.rmq.rmq_url)
app = FastStream(broker)
broker.include_routers(rmq_order_router)

setup_dishka(container, app)
