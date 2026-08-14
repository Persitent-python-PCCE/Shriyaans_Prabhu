from config.db import DataBase
class ProductDAO:

    def __init__(self):
        self.db = DataBase()

    def create_product(
        self,
        category_id,
        product_name,
        unit,
        price,
        stock
    ):

        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO products
                (
                    ProductName,
                    CategoryID,
                    Unit,
                    Price,
                    Stock
                )
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                product_name,
                category_id,
                unit,
                price,
                stock
            )

            cursor.execute(query, values)
            connection.commit()

            return cursor.lastrowid

        except Exception as e:
            connection.rollback()
            print(f"Error creating product: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    def get_product_by_id(self, product_id):

        connection = self.db.connect()

        if connection is None:
            return None

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    p.ProductID AS product_id,
                    p.CategoryID AS category_id,
                    p.ProductName AS product_name,
                    p.Unit AS unit,
                    p.Price AS price,
                    p.Stock AS stock,
                    c.CategoryName AS category_name
                FROM products p
                INNER JOIN categories c
                    ON p.CategoryID = c.CategoryID
                WHERE p.ProductID = %s
            """

            cursor.execute(query, (product_id,))
            return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching product: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

   
    def get_all_products(self):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    p.ProductID AS product_id,
                    p.CategoryID AS category_id,
                    p.ProductName AS product_name,
                    p.Unit AS unit,
                    p.Price AS price,
                    p.Stock AS stock,
                    c.CategoryName AS category_name
                FROM products p
                INNER JOIN categories c
                    ON p.CategoryID = c.CategoryID
                ORDER BY p.ProductID
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching products: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

  

    def get_all_categories(self):

        connection = self.db.connect()

        if connection is None:
            return []

        cursor = connection.cursor(dictionary=True)

        try:
            query = """
                SELECT
                    CategoryID AS category_id,
                    CategoryName AS category_name,
                    Description AS description
                FROM categories
                ORDER BY CategoryName
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error fetching categories: {e}")
            return []

        finally:
            cursor.close()
            connection.close()

    

    def update_product(
        self,
        product_id,
        category_id,
        product_name,
        unit,
        price
    ):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            query = """
                UPDATE products
                SET
                    CategoryID = %s,
                    ProductName = %s,
                    Unit = %s,
                    Price = %s
                WHERE ProductID = %s
            """

            values = (
                category_id,
                product_name,
                unit,
                price,
                product_id
            )

            cursor.execute(query, values)
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error updating product: {e}")
            return False

        finally:
            cursor.close()
            connection.close()

    def update_stock(self, product_id, stock):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            query = """
                UPDATE products
                SET Stock = %s
                WHERE ProductID = %s
            """

            cursor.execute(query, (stock, product_id))
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error updating stock: {e}")
            return False

        finally:
            cursor.close()
            connection.close()


    def delete_product(self, product_id):

        connection = self.db.connect()

        if connection is None:
            return False

        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM products
                WHERE ProductID = %s
            """

            cursor.execute(query, (product_id,))
            connection.commit()

            return cursor.rowcount > 0

        except Exception as e:
            connection.rollback()
            print(f"Error deleting product: {e}")
            return False

        finally:
            cursor.close()
            connection.close()