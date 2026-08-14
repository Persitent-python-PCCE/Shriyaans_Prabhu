from service.cart_service import CartService
from service.order_service import OrderService
class CartController:

    def __init__(self):
        self.cart_service = CartService()
        self.order_service = OrderService()

    

    def display_cart(self, customer):

        cart = self.cart_service.get_cart(
            customer.user_id
        )

        print("\n" + "=" * 80)
        print("                         SHOPPING CART")
        print("=" * 80)

        if not cart.items:

            print("Your cart is empty.")
            print("=" * 80)

            return

        for item in cart.items:

            subtotal = (
                item["unit_price"] *
                item["quantity"]
            )

            print(
                f"Product ID : {item['product_id']}"
            )

            print(
                f"Product    : {item['product_name']}"
            )

            print(
                f"Quantity   : {item['quantity']}"
            )

            print(
                f"Unit Price : ₹{item['unit_price']:.2f}"
            )

            print(
                f"Subtotal   : ₹{subtotal:.2f}"
            )

            print("-" * 80)

        total = self.cart_service.get_total(
            customer.user_id
        )

        total_items = self.cart_service.get_total_items(
            customer.user_id
        )

        print(
            f"Total Items : {total_items}"
        )

        print(
            f"Cart Total  : ₹{total:.2f}"
        )

        print("=" * 80)

    

    def add_item(self, customer):

        print("\n" + "=" * 40)
        print("             ADD TO CART")
        print("=" * 40)

        try:

            product_id = int(
                input("Enter product ID: ")
            )

            quantity = int(
                input("Enter quantity: ")
            )

            return self.cart_service.add_item(
                customer.user_id,
                product_id,
                quantity
            )

        except ValueError:

            print(
                "Please enter valid numbers."
            )

            return False

    

    def update_item(self, customer):

        print("\n" + "=" * 40)
        print("           UPDATE CART ITEM")
        print("=" * 40)

        try:

            product_id = int(
                input("Enter product ID: ")
            )

            quantity = int(
                input("Enter new quantity: ")
            )

            return self.cart_service.update_item(
                customer.user_id,
                product_id,
                quantity
            )

        except ValueError:

            print(
                "Please enter valid numbers."
            )

            return False

    

    def remove_item(self, customer):

        print("\n" + "=" * 40)
        print("          REMOVE FROM CART")
        print("=" * 40)

        try:

            product_id = int(
                input("Enter product ID: ")
            )

            return self.cart_service.remove_item(
                customer.user_id,
                product_id
            )

        except ValueError:

            print(
                "Please enter a valid product ID."
            )

            return False

   
    def clear_cart(self, customer):

        confirm = input(
            "Are you sure you want to clear the cart? (y/n): "
        ).strip().lower()

        if confirm != "y":

            print("Clear cancelled.")
            return False

        return self.cart_service.clear_cart(
            customer.user_id
        )

    

    def place_order(self, customer):

        print("\n" + "=" * 50)
        print("                PLACE ORDER")
        print("=" * 50)

        cart = self.cart_service.get_cart(customer.user_id)

        if not cart.items:
            print("Your cart is empty. Cannot place order.")
            return

        self.display_cart(customer)

        confirm = input(
            "\nDo you want to place this order? (y/n): "
        ).strip().lower()

        if confirm != "y":
            print("Order cancelled.")
            return

        order = self.cart_service.place_order_from_cart(
            customer.user_id
        )

        if order:
            self.display_order(order)

    

    def display_order(self, order):

        print("\n" + "=" * 70)
        print("                         ORDER")
        print("=" * 70)

        print(f"Order ID    : {order.order_id}")
        print(f"Customer ID : {order.customer_id}")
        print(f"Order Date  : {order.order_date}")
        print(f"Status      : {order.status}")
        print(f"Total       : ₹{order.total_amount:.2f}")

        print("\nItems:")
        print("-" * 70)

        for detail in order.details:
            print(
                f"{detail.product_name} | "
                f"Qty: {detail.quantity} | "
                f"Unit Price: ₹{detail.unit_price:.2f} | "
                f"Subtotal: ₹{detail.get_subtotal():.2f}"
            )

        print("=" * 70)

    

    def display_order_history(self, customer):

        print("\n" + "=" * 60)
        print("                  ORDER HISTORY")
        print("=" * 60)

        orders = self.order_service.get_customer_orders(
            customer.user_id
        )

        if not orders:
            print("No orders found.")
            print("=" * 60)
            return

        for order in orders:
            print(
                f"\nOrder ID: {order.order_id} | "
                f"Date: {order.order_date} | "
                f"Total: ₹{order.total_amount:.2f} | "
                f"Status: {order.status}"
            )

        print("=" * 60)

   

    def view_order(self, customer):

        try:
            order_id = int(
                input("\nEnter order ID: ")
            )

            order = self.order_service.get_order(order_id)

            if order is None:
                return

            if order.customer_id != customer.user_id:
                print("You are not allowed to view this order.")
                return

            self.display_order(order)

        except ValueError:
            print("Invalid order ID.")

    

    def show_cart_menu(self, customer):

        while True:

            print("\n" + "=" * 50)
            print("          CART & ORDER MANAGEMENT")
            print("=" * 50)

            print("1. View Cart")
            print("2. Add Product")
            print("3. Update Quantity")
            print("4. Remove Product")
            print("5. Clear Cart")
            print("6. Place Order")
            print("7. Order History")
            print("8. View Order")
            print("9. Exit")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":

                self.display_cart(customer)

            elif choice == "2":

                self.add_item(customer)

            elif choice == "3":

                self.update_item(customer)

            elif choice == "4":

                self.remove_item(customer)

            elif choice == "5":

                self.clear_cart(customer)

            elif choice == "6":

                self.place_order(customer)

            elif choice == "7":

                self.display_order_history(customer)

            elif choice == "8":

                self.view_order(customer)

            elif choice == "9":

                break

            else:

                print("Invalid choice.")