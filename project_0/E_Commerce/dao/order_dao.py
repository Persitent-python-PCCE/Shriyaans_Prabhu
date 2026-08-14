from decimal import Decimal
from config.db import DataBase
class OrderDAO:

    def __init__(self):
        self.db = DataBase()

  

    def create_order(
        self,
        customer_id,
        items,
        status="PLACED"
    ):
        """
        items format:
        [
            {"product_id": 1, "quantity": 2},
            {"product_id": 3, "quantity": 1}
        ]

        Order creation, order details insertion, and stock
        reduction happen in one transaction.
        """

        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:
            total_amount = Decimal("0.00")
            locked_products = {}

         

            for item in items:

                product_id = item["product_id"]
                quantity = item["quantity"]

                query = """
                    SELECT
                        ProductID AS product_id,
                        ProductName AS product_name,
                        Price AS price,
                        Stock AS stock
                    FROM products
                    WHERE ProductID = %s
                    FOR UPDATE
                """

                cursor.execute(query, (product_id,))
                product = cursor.fetchone()

                if product is None:
                    raise ValueError(
                        f"Product ID {product_id} does not exist."
                    )

                if product["stock"] < quantity:
                    raise ValueError(
                        f"Insufficient stock for "
                        f"'{product['product_name']}'. "
                        f"Available: {product['stock']}, "
                        f"Requested: {quantity}."
                    )

                total_amount += (
                    Decimal(str(product["price"])) * quantity
                )

                locked_products[product_id] = product

            

            order_query = """
                INSERT INTO orders
                (
                    CustomerID,
                    OrderDate,
                    TotalAmount,
                    Status
                )
                VALUES (%s, NOW(), %s, %s)
            """

            cursor.execute(
                order_query,
                (
                    customer_id,
                    total_amount,
                    status
                )
            )

            order_id = cursor.lastrowid

             

            detail_query = """
                INSERT INTO order_details
                (
                    OrderID,
                    ProductID,
                    Quantity,
                    UnitPrice
                )
                VALUES (%s, %s, %s, %s)
            """

            stock_query = """
                UPDATE products
                SET Stock = Stock - %s
                WHERE ProductID = %s
            """

            for item in items:

                product_id = item["product_id"]
                quantity = item["quantity"]

                unit_price = locked_products[product_id]["price"]

                cursor.execute(
                    detail_query,
                    (
                        order_id,
                        product_id,
                        quantity,
                        unit_price
                    )
                )

                cursor.execute(
                    stock_query,
                    (
                        quantity,
                        product_id
                    )
                )

            connection.commit()

            return order_id

        except Exception as e:
            connection.rollback()
            print(f"Error creating order: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    
    def get_order_by_id(self, order_id):

        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    OrderID AS order_id,
                    CustomerID AS customer_id,
                    OrderDate AS order_date,
                    TotalAmount AS total_amount,
                    Status AS status
                FROM orders
                WHERE OrderID = %s
            """

            cursor.execute(query, (order_id,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching order: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

     
    def get_order_details(self, order_id):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    od.OrderDetailID AS order_detail_id,
                    od.OrderID AS order_id,
                    od.ProductID AS product_id,
                    od.Quantity AS quantity,
                    od.UnitPrice AS unit_price,
                    p.ProductName AS product_name
                FROM order_details od
                INNER JOIN products p
                    ON od.ProductID = p.ProductID
                WHERE od.OrderID = %s
                ORDER BY od.OrderDetailID
            """

            cursor.execute(query, (order_id,))
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching order details: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

     

    def get_customer_orders(self, customer_id):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    OrderID AS order_id,
                    CustomerID AS customer_id,
                    OrderDate AS order_date,
                    TotalAmount AS total_amount,
                    Status AS status
                FROM orders
                WHERE CustomerID = %s
                ORDER BY OrderDate DESC, OrderID DESC
            """

            cursor.execute(query, (customer_id,))
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching customer orders: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

  

    def get_all_orders(self):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    o.OrderID AS order_id,
                    o.CustomerID AS customer_id,
                    c.CustomerName AS customer_name,
                    o.OrderDate AS order_date,
                    o.TotalAmount AS total_amount,
                    o.Status AS status
                FROM orders o
                INNER JOIN customers c
                    ON o.CustomerID = c.CustomerID
                ORDER BY o.OrderDate DESC, o.OrderID DESC
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching all orders: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

    

    def update_order_status(self, order_id, status):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            query = """
                UPDATE orders
                SET Status = %s
                WHERE OrderID = %s
            """

            cursor.execute(
                query,
                (
                    status,
                    order_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error updating order status: {e}")
            return False

        finally:
            cursor.close()
            connection.close()