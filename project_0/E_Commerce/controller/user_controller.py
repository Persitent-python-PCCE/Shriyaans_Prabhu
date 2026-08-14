from service.user_service import UserService
from controller.cart_controller import CartController
from controller.order_controller import OrderController
from controller.product_controller import ProductController
import getpass
class UserController:

    def __init__(self):
        self.user_service = UserService()
        self.cart_controller = CartController()
        self.order_controller = OrderController()
        self.product_controller = ProductController()

    

    def register_user(self):

        print("\n" + "=" * 40)
        print("          USER REGISTRATION")
        print("=" * 40)

         
        print("\nSelect your role:")
        print("1. Customer")
        print("2. Admin")

        role_choice = input(
            "\nEnter your role choice (1-2): "
        ).strip()

        if role_choice == "1":
            role = "CUSTOMER"

        elif role_choice == "2":
            role = "ADMIN"

        else:
            print("\nInvalid role choice. Defaulting to CUSTOMER.")
            role = "CUSTOMER"

        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        password =getpass.getpass("Enter password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        
        if password != confirm_password:
            print("\nPasswords do not match.")
            return None

        
        contact_name = None
        address = None
        city = None
        postal_code = None
        country = None

        if role == "CUSTOMER":
            contact_name = input(
                "Enter contact name (optional): "
            ).strip()

            address = input(
                "Enter address (optional): "
            ).strip()

            city = input(
                "Enter city (optional): "
            ).strip()

            postal_code = input(
                "Enter postal code (optional): "
            ).strip()

            country = input(
                "Enter country (optional): "
            ).strip()

        
        user = self.user_service.register(
            name=name,
            email=email,
            password=password,
            contact_name=contact_name if contact_name else None,
            address=address if address else None,
            city=city if city else None,
            postal_code=postal_code if postal_code else None,
            country=country if country else None,
            role=role
        )

        if user:
            print("\nRegistration completed successfully.")
            return user

        print("\nRegistration failed.")
        return None

    
    def delete_account(self, user):

        print("\n" + "=" * 40)
        print("         DELETE ACCOUNT")
        print("=" * 40)

        confirm = input(
            f"\nAre you sure you want to delete account "
            f"for {user.get_full_name()}? (yes/no): "
        ).strip().lower()

        if confirm != "yes":
            print("\nDelete cancelled.")
            return False

        password = input(
            "Enter your password to confirm: "
        )

        success = self.user_service.delete_account(
            user.email,
            password
        )

        if success:
            print("\nAccount deleted successfully.")
            return True

        print("\nFailed to delete account. Invalid password.")
        return False

  

    def login_user(self):

        print("\n" + "=" * 40)
        print("             USER LOGIN")
        print("=" * 40)

        # email = input("Enter email: ").strip()
        name=input("Enter name:").strip()
        password = getpass.getpass("Enter password: ")

        user = self.user_service.login(
            name=name,
            password=password
        )

        if user:
            return user

        return None

  

    def display_profile(self, user):

        if user is None:
            print("No user is currently logged in.")
            return

        print("\n" + "=" * 40)
        print("             USER PROFILE")
        print("=" * 40)

        print(f"User ID : {user.user_id}")
        print(f"Name    : {user.name}")
        print(f"Email   : {user.email}")
        print(f"Role    : {user.get_role()}")

        if user.get_role() == "CUSTOMER":
            print(f"Contact : {user.contact_name}")
            print(f"Address : {user.address}")
            print(f"City    : {user.city}")
            print(f"Postal  : {user.postal_code}")
            print(f"Country : {user.country}")

        print("=" * 40)

   

    def show_user_menu(self, user):
        """
        Display menu based on user role (Admin or Customer).
        Returns updated user (None if logged out or deleted).
        """

        while True:

            print("\n" + "=" * 50)
            print(f"Welcome, {user.get_full_name()}!")
            print(f"Role: {user.get_role()}")
            print("=" * 50)

            if user.get_role() == "ADMIN":

                print("\nOptions:")
                print("1. View Profile")
                print("2. Register New Account")
                print("3. Manage Products")
                print("4. Manage Orders")
                print("5. Delete Account")
                print("6. Logout")
                print("7. Exit Application")

                choice = input(
                    "\nEnter your choice (1-7): "
                ).strip()

                if choice == "1":
                    self.display_profile(user)

                elif choice == "2":
                    new_user = self.register_user()

                    if new_user:
                        print(
                            f"\nNew account registered successfully "
                            f"for {new_user.get_full_name()}!"
                        )

                elif choice == "3":
                    self.product_controller.admin_menu()

                elif choice == "4":
                    self.order_controller.admin_menu()

                elif choice == "5":
                    if self.delete_account(user):
                        return None

                elif choice == "6":
                    print("\nLogging out...")
                    return None

                elif choice == "7":
                    return "EXIT"

                else:
                    print("\nInvalid choice. Please try again.")

            else:
                # CUSTOMER role

                print("\nOptions:")
                print("1. View Profile")
                print("2. Register New Account")
                print("3. View Products")
                print("4. Cart / Place Order")
                print("5. Delete Account")
                print("6. Logout")
                print("7. Exit Application")

                choice = input(
                    "\nEnter your choice (1-7): "
                ).strip()

                if choice == "1":
                    self.display_profile(user)

                elif choice == "2":
                    new_user = self.register_user()

                    if new_user:
                        print(
                            f"\nNew account registered successfully "
                            f"for {new_user.get_full_name()}!"
                        )

                elif choice == "3":
                    self.product_controller.display_products()

                elif choice == "4":
                    self.cart_controller.show_cart_menu(user)

                elif choice == "5":
                    if self.delete_account(user):
                        return None

                elif choice == "6":
                    print("\nLogging out...")
                    return None

                elif choice == "7":
                    return "EXIT"

                else:
                    print("\nInvalid choice. Please try again.")