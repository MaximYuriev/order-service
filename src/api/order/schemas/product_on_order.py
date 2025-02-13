from pydantic import BaseModel


class ProductOnOrderSchema(BaseModel):
    product_id: int
    product_name: str
    quantity_on_order: int
    price_per_piece: int
