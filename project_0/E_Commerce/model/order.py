from decimal import Decimal
class OrderDetail:

    def __init__(
        self,
        order_detail_id,
        order_id,
        product_id,
        quantity,
        unit_price,
        product_name=None
    ):
        self._order_detail_id = order_detail_id
        self._order_id = order_id
        self._product_id = product_id
        self._quantity = quantity
        self._unit_price = Decimal(str(unit_price))
        self._product_name = product_name

    @property
    def order_detail_id(self):
        return self._order_detail_id

    @property
    def order_id(self):
        return self._order_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    @property
    def unit_price(self):
        return self._unit_price

    @property
    def product_name(self):
        return self._product_name

    def get_subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self):
        name = self.product_name or f"Product #{self.product_id}"

        return (
            f"{name} | "
            f"Qty: {self.quantity} | "
            f"Unit Price: ₹{self.unit_price:.2f} | "
            f"Subtotal: ₹{self.get_subtotal():.2f}"
        )


class Order:

    def __init__(
        self,
        order_id,
        customer_id,
        order_date,
        total_amount,
        status,
        details=None
    ):
        self._order_id = order_id
        self._customer_id = customer_id
        self._order_date = order_date
        self._total_amount = Decimal(str(total_amount))
        self._status = status
        self._details = details if details else []

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def order_date(self):
        return self._order_date

    @property
    def total_amount(self):
        return self._total_amount

    @property
    def status(self):
        return self._status

    @property
    def details(self):
        return self._details

    def add_detail(self, detail):
        self._details.append(detail)

    def get_item_count(self):
        return sum(detail.quantity for detail in self._details)

    def display_info(self):
        return {
            "order_id": self._order_id,
            "customer_id": self._customer_id,
            "order_date": self._order_date,
            "total_amount": self._total_amount,
            "status": self._status,
            "item_count": self.get_item_count()
        }

    def __str__(self):
        return (
            f"Order #{self._order_id} | "
            f"Date: {self._order_date} | "
            f"Total: ₹{self._total_amount:.2f} | "
            f"Status: {self._status}"
        )