from controller.user_controller import UserController
def main():
    """Main application entry point"""
    user_controller = UserController()
    current_user = None

    while True:
        # If no user logged in, show login/register menu
        if current_user is None:
            print("\n" + "=" * 50)
            print("    WELCOME TO E-COMMERCE APPLICATION")
            print("=" * 50)

            print("\nOptions:")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == "1":
                user = user_controller.login_user()
                if user:
                    current_user = user
                    print(f"\nLogin successful! Welcome, {user.get_full_name()}!")
                else:
                    print("\nLogin failed. Please check your credentials.")

            elif choice == "2":
                user = user_controller.register_user()
                if user:
                    current_user = user
                    print(f"\nRegistration successful! Welcome, {user.get_full_name()}!")
                else:
                    print("\nRegistration failed.")

            elif choice == "3":
                print("\nThank you for using E-Commerce Application. Goodbye!")
                break

            else:
                print("\nInvalid choice. Please try again.")

        # User is logged in, show user menu
        else:
            result = user_controller.show_user_menu(current_user)
            
            if result == "EXIT":
                print("\nThank you for using E-Commerce Application. Goodbye!")
                break
            else:
                # result is None (logged out) or a new user (from register)
                current_user = result


if __name__ == "__main__":
    main()