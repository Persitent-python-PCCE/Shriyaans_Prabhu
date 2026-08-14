class Cart:
    def __init__(
        self,
        customer_id,
        cart_id=None
    ):
        self._cart_id = cart_id
        self._customer_id = customer_id
        self._items = []
    
    @property
    def cart_id(self):
        return self._cart_id
    @property
    def customer_id(self):
        return self._customer_id
    @property
    def items(self):
        return self._items