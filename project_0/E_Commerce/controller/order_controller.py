from service.order_service import OrderService
class OrderController:

    def __init__(self):
        self.order_service = OrderService()

    # ==========================================
    # PLACE ORDER
    # ==========================================

    def place_order(self, customer):

        print("\n" + "=" * 50)
        print("                PLACE ORDER")
        print("=" * 50)

        cart = []

        while True:

            try:
                product_id = int(
                    input(
                        "\nEnter product ID "
                        "(0 to checkout): "
                    )
                )

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if product_id == 0:
                break

            try:
                quantity = int(
                    input("Enter quantity: ")
                )

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if quantity <= 0:
                print(
                    "Quantity must be greater than zero."
                )
                continue

            cart.append(
                {
                    "product_id": product_id,
                    "quantity": quantity
                }
            )

            print("Product added to order.")

        if not cart:
            print("\nNo products selected.")
            return None

        order = self.order_service.place_order(
            customer_id=customer.user_id,
            items=cart
        )

        if order:
            self.display_order(order)

        return order

    # ==========================================
    # DISPLAY ORDER
    # ==========================================

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

    # ==========================================
    # CUSTOMER ORDER HISTORY
    # ==========================================

    def order_history(self, customer):

        print("\n" + "=" * 60)
        print("                  ORDER HISTORY")
        print("=" * 60)

        orders = self.order_service.get_customer_orders(
            customer.user_id
        )

        if not orders:
            print("No orders found.")
            return

        for order in orders:
            print(
                f"\nOrder ID: {order.order_id} | "
                f"Date: {order.order_date} | "
                f"Total: ₹{order.total_amount:.2f} | "
                f"Status: {order.status}"
            )

    # ==========================================
    # VIEW SINGLE ORDER
    # ==========================================

    def view_order(self, customer=None):

        try:
            order_id = int(
                input("\nEnter order ID: ")
            )

            order = self.order_service.get_order(order_id)

            if order is None:
                return

            # Customer may only view their own order.
            if customer is not None:
                if order.customer_id != customer.user_id:
                    print(
                        "You are not allowed to view "
                        "this order."
                    )
                    return

            self.display_order(order)

        except ValueError:
            print("Invalid order ID.")

    # ==========================================
    # ADMIN - ALL ORDERS
    # ==========================================

    def display_all_orders(self):

        print("\n" + "=" * 90)
        print("                         ALL ORDERS")
        print("=" * 90)

        orders = self.order_service.get_all_orders()

        if not orders:
            print("No orders found.")
            return

        for order in orders:
            print(
                f"Order ID: {order['order_id']} | "
                f"Customer ID: {order['customer_id']} | "
                f"Customer: {order['customer_name']} | "
                f"Date: {order['order_date']} | "
                f"Total: ₹{order['total_amount']:.2f} | "
                f"Status: {order['status']}"
            )

    # ==========================================
    # ADMIN - UPDATE STATUS
    # ==========================================

    def update_status(self):

        try:
            order_id = int(
                input("\nEnter order ID: ")
            )

            print("\nAvailable statuses:")
            print("1. PLACED")
            print("2. PROCESSING")
            print("3. SHIPPED")
            print("4. DELIVERED")
            print("5. CANCELLED")

            choice = input(
                "\nEnter status choice (1-5): "
            ).strip()

            statuses = {
                "1": "PLACED",
                "2": "PROCESSING",
                "3": "SHIPPED",
                "4": "DELIVERED",
                "5": "CANCELLED"
            }

            status = statuses.get(choice)

            if status is None:
                print("Invalid status choice.")
                return False

            return self.order_service.update_order_status(
                order_id,
                status
            )

        except ValueError:
            print("Invalid order ID.")
            return False

    # ==========================================
    # CUSTOMER ORDER MENU
    # ==========================================

    def customer_menu(self, customer):

        while True:

            print("\n" + "=" * 45)
            print("                ORDER MENU")
            print("=" * 45)

            print("1. Place Order")
            print("2. Order History")
            print("3. View Order")
            print("4. Exit")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":
                self.place_order(customer)

            elif choice == "2":
                self.order_history(customer)

            elif choice == "3":
                self.view_order(customer)

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    # ==========================================
    # ADMIN ORDER MENU
    # ==========================================

    def admin_menu(self):

        while True:

            print("\n" + "=" * 45)
            print("             ORDER MANAGEMENT")
            print("=" * 45)

            print("1. View All Orders")
            print("2. View Order")
            print("3. Update Order Status")
            print("4. Exit")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":
                self.display_all_orders()

            elif choice == "2":
                self.view_order()

            elif choice == "3":
                self.update_status()

            elif choice == "4":
                break

            else:
                print("Invalid choice.")