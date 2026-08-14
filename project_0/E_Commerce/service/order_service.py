from dao.order_dao import OrderDAO
from model.order import Order, OrderDetail
class OrderService:

    def __init__(self):
        self.order_dao = OrderDAO()

    

    def validate_order(self, customer_id, items):

        if not customer_id:
            print("Customer ID is required.")
            return False

        if not items:
            print("Cart is empty.")
            return False

        for item in items:

            if "product_id" not in item:
                print("Product ID is missing.")
                return False

            if "quantity" not in item:
                print("Quantity is missing.")
                return False

            if not isinstance(item["quantity"], int):
                print("Quantity must be an integer.")
                return False

            if item["quantity"] <= 0:
                print("Quantity must be greater than zero.")
                return False

        return True

    
    def place_order(self, customer_id, items):

        if not self.validate_order(customer_id, items):
            return None

        order_id = self.order_dao.create_order(
            customer_id=customer_id,
            items=items,
            status="PLACED"
        )

        if order_id is None:
            print("Order placement failed.")
            return None

        order = self.get_order(order_id)

        if order:
            print(
                f"Order placed successfully! "
                f"Order ID: {order.order_id}"
            )

        return order

 

    def get_order(self, order_id):

        order_data = self.order_dao.get_order_by_id(order_id)

        if order_data is None:
            print("Order not found.")
            return None

        detail_data = self.order_dao.get_order_details(order_id)

        details = []

        for data in detail_data:
            details.append(
                OrderDetail(
                    order_detail_id=data["order_detail_id"],
                    order_id=data["order_id"],
                    product_id=data["product_id"],
                    quantity=data["quantity"],
                    unit_price=data["unit_price"],
                    product_name=data["product_name"]
                )
            )

        return self._create_order_object(
            order_data,
            details
        )

     

    def get_customer_orders(self, customer_id):

        order_data = self.order_dao.get_customer_orders(
            customer_id
        )

        orders = []

        for data in order_data:

            details = self.order_dao.get_order_details(
                data["order_id"]
            )

            detail_objects = []

            for detail in details:
                detail_objects.append(
                    OrderDetail(
                        order_detail_id=detail["order_detail_id"],
                        order_id=detail["order_id"],
                        product_id=detail["product_id"],
                        quantity=detail["quantity"],
                        unit_price=detail["unit_price"],
                        product_name=detail["product_name"]
                    )
                )

            orders.append(
                self._create_order_object(
                    data,
                    detail_objects
                )
            )

        return orders

    

    def get_all_orders(self):
        return self.order_dao.get_all_orders()

    

    def update_order_status(self, order_id, status):

        allowed_statuses = [
            "PLACED",
            "PROCESSING",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED"
        ]

        status = status.strip().upper()

        if status not in allowed_statuses:
            print("Invalid order status.")
            print(
                "Allowed statuses:",
                ", ".join(allowed_statuses)
            )
            return False

        order = self.order_dao.get_order_by_id(order_id)

        if order is None:
            print("Order not found.")
            return False

        success = self.order_dao.update_order_status(
            order_id,
            status
        )

        if success:
            print("Order status updated successfully.")

        return success

 

    def _create_order_object(self, data, details):

        return Order(
            order_id=data["order_id"],
            customer_id=data["customer_id"],
            order_date=data["order_date"],
            total_amount=data["total_amount"],
            status=data["status"],
            details=details
        )