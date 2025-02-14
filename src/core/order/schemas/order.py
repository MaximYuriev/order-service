import uuid
from abc import ABC

from pydantic import BaseModel


class OrderBrokerSchema(BaseModel, ABC):
    pass


class PrepareOrderBrokerSchema(OrderBrokerSchema):
    order_id: uuid.UUID
    user_id: uuid.UUID
