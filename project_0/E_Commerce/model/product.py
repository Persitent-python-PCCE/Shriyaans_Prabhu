class Product:
    def __init__(
        self,
        product_id,
        category_id,
        product_name,
        unit,
        price,
        stock=0,
        category_name=None
    ):
        self._product_id = product_id
        self._category_id = category_id
        self._product_name = product_name
        self._unit = unit
        self._price = price
        self._stock = stock
        self._category_name = category_name

   

    @property
    def product_id(self):
        return self._product_id

    @property
    def category_id(self):
        return self._category_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def unit(self):
        return self._unit

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @property
    def category_name(self):
        return self._category_name

    # METHODS

    def is_available(self):
        return self._stock > 0

    def display_info(self):
        return {
            "product_id": self._product_id,
            "name": self._product_name,
            "category": self._category_name,
            "unit": self._unit,
            "price": self._price,
            "stock": self._stock,
            "available": self.is_available()
        }

    def __str__(self):
        return (
            f"[{self._product_id}] "
            f"{self._product_name} "
            f"- ₹{self._price:.2f} "
            f"(Stock: {self._stock})"
        )