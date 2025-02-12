import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.core.commons.model import Base
from src.core.order.models.order import OrderModel


class ProductOnOrderModel(Base):
    __tablename__ = "product_on_order"
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(OrderModel.order_id), primary_key=True)
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str]
    quantity_in_order: Mapped[int]
    price_per_piece: Mapped[int]
