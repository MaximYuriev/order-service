import uuid

from sqlalchemy.orm import Mapped, mapped_column

from src.core.commons.model import Base


class OrderModel(Base):
    __tablename__ = "order"
    order_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID]
    order_price: Mapped[int] = mapped_column(nullable=True)
    order_status: Mapped[str]
