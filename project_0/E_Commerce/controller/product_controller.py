from service.product_service import ProductService
class ProductController:

    def __init__(self):
        self.product_service = ProductService()

    # ==========================================
    # DISPLAY PRODUCTS
    # ==========================================

    def display_products(self):

        products = self.product_service.get_all_products()

        if not products:
            print("\nNo products available.")
            return

        print("\n" + "=" * 90)
        print("                              PRODUCTS")
        print("=" * 90)

        for product in products:

            print(
                f"ID: {product.product_id} | "
                f"{product.product_name}"
            )

            print(
                f"Category: {product.category_name} | "
                f"Unit: {product.unit}"
            )

            print(
                f"Price: ₹{product.price:.2f} | "
                f"Stock: {product.stock}"
            )

            print(
                f"Available: "
                f"{'Yes' if product.is_available() else 'No'}"
            )

            print("-" * 90)

    # ==========================================
    # ADD PRODUCT
    # ==========================================

    def add_product(self):

        print("\n" + "=" * 40)
        print("             ADD PRODUCT")
        print("=" * 40)

        try:
            categories = self.product_service.get_all_categories()

            if not categories:
                print("No categories available.")
                return

            print("\nAvailable Categories:")

            for category in categories:
                print(
                    f"{category['category_id']} - "
                    f"{category['category_name']}"
                )

            category_id = int(
                input("Enter category ID: ")
            )

            product_name = input(
                "Enter product name: "
            ).strip()

            unit = input(
                "Enter unit (e.g. pcs, kg, box): "
            ).strip()

            price = float(
                input("Enter price: ")
            )

            stock = int(
                input("Enter stock quantity: ")
            )

            product = self.product_service.add_product(
                category_id=category_id,
                product_name=product_name,
                unit=unit,
                price=price,
                stock=stock
            )

            if product:
                print("\nProduct details:")
                print(product)

        except ValueError:
            print(
                "\nInvalid input. "
                "Please enter valid numbers."
            )

    # ==========================================
    # UPDATE PRODUCT
    # ==========================================

    def update_product(self):

        print("\n" + "=" * 40)
        print("           UPDATE PRODUCT")
        print("=" * 40)

        try:
            product_id = int(
                input("Enter product ID: ")
            )

            categories = self.product_service.get_all_categories()

            if not categories:
                print("No categories available.")
                return

            print("\nAvailable Categories:")

            for category in categories:
                print(
                    f"{category['category_id']} - "
                    f"{category['category_name']}"
                )

            category_id = int(
                input("Enter new category ID: ")
            )

            product_name = input(
                "Enter new product name: "
            ).strip()

            unit = input(
                "Enter new unit: "
            ).strip()

            price = float(
                input("Enter new price: ")
            )

            self.product_service.update_product(
                product_id=product_id,
                category_id=category_id,
                product_name=product_name,
                unit=unit,
                price=price
            )

        except ValueError:
            print(
                "\nInvalid input. "
                "Please enter valid numbers."
            )

    # ==========================================
    # UPDATE STOCK
    # ==========================================

    def update_stock(self):

        print("\n" + "=" * 40)
        print("           UPDATE STOCK")
        print("=" * 40)

        try:
            product_id = int(
                input("Enter product ID: ")
            )

            stock = int(
                input("Enter new stock quantity: ")
            )

            success = self.product_service.update_stock(
                product_id,
                stock
            )

            if success:
                print("Stock updated successfully.")

        except ValueError:
            print(
                "\nInvalid input. "
                "Please enter a valid number."
            )

    # ==========================================
    # DELETE PRODUCT
    # ==========================================

    def delete_product(self):

        print("\n" + "=" * 40)
        print("           DELETE PRODUCT")
        print("=" * 40)

        try:
            product_id = int(
                input("Enter product ID: ")
            )

            confirm = input(
                "Are you sure? (y/n): "
            ).strip().lower()

            if confirm != "y":
                print("Delete cancelled.")
                return

            self.product_service.delete_product(product_id)

        except ValueError:
            print("\nInvalid product ID.")

    # ==========================================
    # PRODUCT DETAILS
    # ==========================================

    def view_product(self):

        try:
            product_id = int(
                input("\nEnter product ID: ")
            )

            product = self.product_service.get_product(product_id)

            if product:

                print("\n" + "=" * 50)
                print("              PRODUCT")
                print("=" * 50)

                print(f"ID          : {product.product_id}")
                print(f"Category    : {product.category_name}")
                print(f"Name        : {product.product_name}")
                print(f"Unit        : {product.unit}")
                print(f"Price       : ₹{product.price:.2f}")
                print(f"Stock       : {product.stock}")
                print(
                    f"Available   : "
                    f"{'Yes' if product.is_available() else 'No'}"
                )

        except ValueError:
            print("Invalid product ID.")

    # ==========================================
    # ADMIN PRODUCT MENU
    # ==========================================

    def admin_menu(self):

        while True:

            print("\n" + "=" * 45)
            print("             PRODUCT MANAGEMENT")
            print("=" * 45)

            print("1. View Products")
            print("2. View Product Details")
            print("3. Add Product")
            print("4. Update Product")
            print("5. Update Stock")
            print("6. Delete Product")
            print("7. Exit")

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":
                self.display_products()

            elif choice == "2":
                self.view_product()

            elif choice == "3":
                self.add_product()

            elif choice == "4":
                self.update_product()

            elif choice == "5":
                self.update_stock()

            elif choice == "6":
                self.delete_product()

            elif choice == "7":
                print("Exiting product management.")
                break

            else:
                print("Invalid choice.")