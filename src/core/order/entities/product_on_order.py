from dataclasses import dataclass


@dataclass
class ProductOnOrder:
    order_id: int
    product_id: int
    product_name: str
    quantity_in_order: int
    price_per_piece: int
