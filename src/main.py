from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.api.order.router import order_router
from src.config import Config
from src.ioc import OrderProvider, SQLAlchemyProvider, RMQProvider

config = Config()
container = make_async_container(
    OrderProvider(),
    SQLAlchemyProvider(),
    RMQProvider(),
    context={Config: config},
)
app = FastAPI(title="Order Service")
app.include_router(order_router)

setup_dishka(container, app)
