import uuid
from abc import ABC

from pydantic import BaseModel


class OrderBrokerSchema(BaseModel, ABC):
    pass


class PrepareOrderBrokerSchema(OrderBrokerSchema):
    order_id: uuid.UUID
    basket_id: uuid.UUID
