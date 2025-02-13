import uuid
from abc import ABC

from pydantic import BaseModel


class OrderBrokerSchema(BaseModel, ABC):
    pass


class PrepareOrderBrokerSchema(OrderBrokerSchema):
    user_id: uuid.UUID
