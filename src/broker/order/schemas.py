import uuid

from pydantic import BaseModel


class CanceledOrderSchema(BaseModel):
    order_id: uuid.UUID
    reason: str
