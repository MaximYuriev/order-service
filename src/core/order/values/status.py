from enum import Enum


class OrderStatus(Enum):
    ACCEPT = "Заказ принят"
    PREPARE = "Заказ в обработке"
    CANCEL = "Заказ отменен"