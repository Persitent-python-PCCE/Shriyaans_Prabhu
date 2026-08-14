from config.db import DataBase
class CartDAO:

    def __init__(self):
        self.db = DataBase()
    def get_cart(self, customer_id):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:

            query = """
                SELECT
                    c.CartID AS cart_id,
                    c.CustomerID AS customer_id,
                    c.ProductID AS product_id,
                    p.ProductName AS product_name,
                    c.Quantity AS quantity,
                    p.Price AS unit_price,
                    p.Stock AS stock
                FROM cart c
                INNER JOIN products p
                    ON c.ProductID = p.ProductID
                WHERE c.CustomerID = %s
                ORDER BY c.CartID
            """

            cursor.execute(query, (customer_id,))

            return cursor.fetchall()

        except Exception as e:

            print(f"Error fetching cart: {e}")
            return []

        finally:

            cursor.close()
            connection.close()

   

    def get_cart_item(
        self,
        customer_id,
        product_id
    ):

        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:

            query = """
                SELECT
                    CartID AS cart_id,
                    CustomerID AS customer_id,
                    ProductID AS product_id,
                    Quantity AS quantity
                FROM cart
                WHERE CustomerID = %s
                AND ProductID = %s
            """

            cursor.execute(
                query,
                (
                    customer_id,
                    product_id
                )
            )

            return cursor.fetchone()

        except Exception as e:

            print(f"Error fetching cart item: {e}")
            return None

        finally:

            cursor.close()
            connection.close()

     
 
    def add_item(
        self,
        customer_id,
        product_id,
        quantity
    ):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:

            query = """
                INSERT INTO cart
                (
                    CustomerID,
                    ProductID,
                    Quantity
                )
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    Quantity = Quantity + VALUES(Quantity)
            """

            cursor.execute(
                query,
                (
                    customer_id,
                    product_id,
                    quantity
                )
            )

            connection.commit()

            return True

        except Exception as e:

            connection.rollback()
            print(f"Error adding item to cart: {e}")

            return False

        finally:

            cursor.close()
            connection.close()

    
    def update_item(
        self,
        customer_id,
        product_id,
        quantity
    ):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:

            query = """
                UPDATE cart
                SET Quantity = %s
                WHERE CustomerID = %s
                AND ProductID = %s
            """

            cursor.execute(
                query,
                (
                    quantity,
                    customer_id,
                    product_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            connection.rollback()
            print(f"Error updating cart: {e}")

            return False

        finally:

            cursor.close()
            connection.close()

    

    def remove_item(
        self,
        customer_id,
        product_id
    ):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:

            query = """
                DELETE FROM cart
                WHERE CustomerID = %s
                AND ProductID = %s
            """

            cursor.execute(
                query,
                (
                    customer_id,
                    product_id
                )
            )

            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:

            connection.rollback()
            print(f"Error removing cart item: {e}")

            return False

        finally:

            cursor.close()
            connection.close()

  
    def clear_cart(self, customer_id):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:

            query = """
                DELETE FROM cart
                WHERE CustomerID = %s
            """

            cursor.execute(query, (customer_id,))

            connection.commit()

            return True

        except Exception as e:

            connection.rollback()
            print(f"Error clearing cart: {e}")

            return False

        finally:

            cursor.close()
            connection.close()