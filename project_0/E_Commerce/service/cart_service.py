from dao.cart_dao import CartDAO
from dao.product_dao import ProductDAO
# from dao.order_dao import OrderDAO
from model.cart import Cart
from service.order_service import OrderService
class CartService:

    def __init__(self):
        self.cart_dao = CartDAO()
        self.product_dao = ProductDAO()
        self.order_service = OrderService()

 
    def get_cart(self, customer_id):

        cart_data = self.cart_dao.get_cart(
            customer_id
        )

        cart = Cart(customer_id)

        cart.items.extend(cart_data)

        return cart

  
    def add_item(
        self,
        customer_id,
        product_id,
        quantity
    ):

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        # Get product
        product = self.product_dao.get_product_by_id(
            product_id
        )

        if product is None:
            print("Product not found.")
            return False

        # Check stock
        if product["stock"] <= 0:
            print("Product is out of stock.")
            return False

        # Check existing quantity
        cart_item = self.cart_dao.get_cart_item(
            customer_id,
            product_id
        )

        current_quantity = 0

        if cart_item:
            current_quantity = cart_item["quantity"]

        # Check total quantity
        if current_quantity + quantity > product["stock"]:

            print(
                f"Insufficient stock. "
                f"Available stock: {product['stock']}."
            )

            return False

        success = self.cart_dao.add_item(
            customer_id,
            product_id,
            quantity
        )

        if success:
            print("Product added to cart.")

        return success

     

    def remove_item(
        self,
        customer_id,
        product_id
    ):

        success = self.cart_dao.remove_item(
            customer_id,
            product_id
        )

        if success:
            print("Product removed from cart.")
        else:
            print("Product is not in the cart.")

        return success

    def update_item(
        self,
        customer_id,
        product_id,
        quantity
    ):

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        product = self.product_dao.get_product_by_id(
            product_id
        )

        if product is None:
            print("Product not found.")
            return False

         
        if quantity > product["stock"]:

            print(
                f"Insufficient stock. "
                f"Available stock: {product['stock']}."
            )

            return False

    
        cart_item = self.cart_dao.get_cart_item(
            customer_id,
            product_id
        )

        if cart_item is None:

            print("Product is not in the cart.")
            return False

        success = self.cart_dao.update_item(
            customer_id,
            product_id,
            quantity
        )

        if success:
            print("Cart updated successfully.")

        return success

    

    def clear_cart(self, customer_id):

        success = self.cart_dao.clear_cart(
            customer_id
        )

        if success:
            print("Cart cleared.")

        return success

  

    def get_total(self, customer_id):

        cart = self.get_cart(customer_id)

        total = 0

        for item in cart.items:

            total += (
                item["unit_price"] *
                item["quantity"]
            )

        return total

   

    def get_total_items(self, customer_id):

        cart = self.get_cart(customer_id)

        total = 0

        for item in cart.items:
            total += item["quantity"]

        return total


    def place_order_from_cart(self, customer_id):

        cart = self.get_cart(customer_id)

        if not cart.items:
            print("Cart is empty. Cannot place order.")
            return None

        order = self.order_service.place_order(
            customer_id=customer_id,
            items=cart.items
        )

        if order:
            self.clear_cart(customer_id)

        return order