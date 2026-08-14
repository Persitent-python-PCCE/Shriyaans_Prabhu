from dao.product_dao import ProductDAO
from model.product import Product


class ProductService:

    def __init__(self):
        self.product_dao = ProductDAO()

    # ==========================================
    # VALIDATION
    # ==========================================

    def validate_product(
        self,
        product_name,
        price,
        stock
    ):

        if not product_name or not product_name.strip():
            print("Product name cannot be empty.")
            return False

        if price < 0:
            print("Price cannot be negative.")
            return False

        if stock < 0:
            print("Stock cannot be negative.")
            return False

        return True

    # ==========================================
    # CREATE
    # ==========================================

    def add_product(
        self,
        category_id,
        product_name,
        unit,
        price,
        stock
    ):

        if not self.validate_product(
            product_name,
            price,
            stock
        ):
            return None

        product_id = self.product_dao.create_product(
            category_id=category_id,
            product_name=product_name.strip(),
            unit=unit.strip() if unit else None,
            price=price,
            stock=stock
        )

        if product_id is None:
            print("Product creation failed.")
            return None

        print("Product created successfully.")

        return self.get_product(product_id)

    # ==========================================
    # READ ONE
    # ==========================================

    def get_product(self, product_id):

        product_data = self.product_dao.get_product_by_id(product_id)

        if product_data is None:
            print("Product not found.")
            return None

        return self._create_product_object(product_data)

    # ==========================================
    # READ ALL
    # ==========================================

    def get_all_products(self):

        product_data = self.product_dao.get_all_products()

        products = []

        for data in product_data:
            products.append(
                self._create_product_object(data)
            )

        return products

    # ==========================================
    # UPDATE
    # ==========================================

    def update_product(
        self,
        product_id,
        category_id,
        product_name,
        unit,
        price
    ):

        if not product_name or not product_name.strip():
            print("Product name cannot be empty.")
            return False

        if price < 0:
            print("Price cannot be negative.")
            return False

        product = self.product_dao.get_product_by_id(product_id)

        if product is None:
            print("Product not found.")
            return False

        success = self.product_dao.update_product(
            product_id=product_id,
            category_id=category_id,
            product_name=product_name.strip(),
            unit=unit.strip() if unit else None,
            price=price
        )

        if success:
            print("Product updated successfully.")

        return success

    # ==========================================
    # UPDATE STOCK
    # ==========================================

    def update_stock(self, product_id, stock):

        if stock < 0:
            print("Stock cannot be negative.")
            return False

        product = self.product_dao.get_product_by_id(product_id)

        if product is None:
            print("Product not found.")
            return False

        success = self.product_dao.update_stock(
            product_id,
            stock
        )

        if success:
            print("Stock updated successfully.")

        return success

    # ==========================================
    # DELETE
    # ==========================================

    def delete_product(self, product_id):

        product = self.product_dao.get_product_by_id(product_id)

        if product is None:
            print("Product not found.")
            return False

        success = self.product_dao.delete_product(product_id)

        if success:
            print("Product deleted successfully.")

        return success

    # ==========================================
    # CATEGORIES
    # ==========================================

    def get_all_categories(self):
        return self.product_dao.get_all_categories()

    # ==========================================
    # CREATE PRODUCT OBJECT
    # ==========================================

    def _create_product_object(self, data):

        return Product(
            product_id=data["product_id"],
            category_id=data["category_id"],
            product_name=data["product_name"],
            unit=data["unit"],
            price=data["price"],
            stock=data["stock"],
            category_name=data["category_name"]
        )