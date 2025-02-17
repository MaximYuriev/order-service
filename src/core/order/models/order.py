import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.commons.model import Base
from src.core.order.entities.order import Order, CanceledOrder
from src.core.order.values.status import OrderStatus


class OrderModel(Base):
    __tablename__ = "order"
    order_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID]
    order_price: Mapped[int] = mapped_column(nullable=True)
    order_status: Mapped[str]

    @classmethod
    def from_entity(cls, order: Order) -> "OrderModel":
        return cls(
            order_id=order.order_id,
            user_id=order.user_id,
            order_price=order.order_price,
            order_status=order.order_status,
        )

    def to_entity(self) -> Order:
        return Order(
            order_id=self.order_id,
            user_id=self.user_id,
            order_price=self.order_price,
            order_status=OrderStatus(self.order_status),
        )


class CanceledOrderModel(Base):
    __tablename__ = "canceled_order"
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(OrderModel.order_id), primary_key=True)
    reason: Mapped[str]

    @classmethod
    def from_entity(cls, canceled_order: CanceledOrder) -> "CanceledOrderModel":
        return cls(
            order_id=canceled_order.order_id,
            reason=canceled_order.reason,
        )

    def to_entity(self) -> CanceledOrder:
        return CanceledOrder(
            order_id=self.order_id,
            reason=self.reason,
        )
