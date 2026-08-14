import re
from dao.user_dao import UserDAO
from model.user import Customer, Admin
from utils.password import hash_password, verify_password
class UserService:

    def __init__(self):
        self.user_dao = UserDAO()

    

    def validate_email(self, email):
        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        return len(password) >= 8

    

    def register(
        self,
        name,
        email,
        password,
        contact_name=None,
        address=None,
        city=None,
        postal_code=None,
        country=None,
        role="CUSTOMER"
    ):
       
        if not name.strip():
            print("Name cannot be empty.")
            return None

        if not self.validate_email(email):
            print("Invalid email address.")
            return None

        if not self.validate_password(password):
            print("Password must contain at least 8 characters.")
            return None

        email = email.strip().lower()
        role = role.upper()

        
        if role not in ["ADMIN", "CUSTOMER"]:
            print("Invalid role. Defaulting to CUSTOMER.")
            role = "CUSTOMER"

         
        existing_user = self.user_dao.get_user_by_email(email)

        if existing_user:
            print("Email already registered.")
            return None

        

        password_hash = hash_password(password)

         

        if role == "ADMIN":
            user_id = self.user_dao.create_admin(
                name=name.strip(),
                email=email,
                password_hash=password_hash
            )

        else:
            user_id = self.user_dao.create_customer(
                name=name.strip(),
                email=email,
                password_hash=password_hash,
                contact_name=contact_name.strip() if contact_name else None,
                address=address.strip() if address else None,
                city=city.strip() if city else None,
                postal_code=postal_code.strip() if postal_code else None,
                country=country.strip() if country else None
            )

        if user_id is None:
            print("Registration failed.")
            return None

        print("Registration successful!")
        print(f"User ID: {user_id}")

         
        if role == "ADMIN":
            return Admin(
                user_id=user_id,
                name=name.strip(),
                email=email
            )

        return Customer(
            user_id=user_id,
            name=name.strip(),
            email=email,
            contact_name=contact_name.strip() if contact_name else None,
            address=address.strip() if address else None,
            city=city.strip() if city else None,
            postal_code=postal_code.strip() if postal_code else None,
            country=country.strip() if country else None
        )

   

    def login(self, name, password):

        # email = email.strip().lower()
        name=name.strip().lower()

      
        # user_data = self.user_dao.get_user_by_email(email)
        user_data=self.user_dao.get_user_by_name(name)

        if user_data is None:
            print("Invalid email or password.")
            return None

        
        if not verify_password(
            password,
            user_data["password_hash"]
        ):
            print("Invalid email or password.")
            return None

       

        if user_data["role_name"] == "ADMIN":
            user = Admin(
                user_id=user_data["user_id"],
                name=user_data["name"],
                email=user_data["email"]
            )

        else:
            user = Customer(
                user_id=user_data["user_id"],
                name=user_data["name"],
                email=user_data["email"],
                contact_name=user_data["contact_name"],
                address=user_data["address"],
                city=user_data["city"],
                postal_code=user_data["postal_code"],
                country=user_data["country"]
            )

        print(
            f"Login successful. "
            f"Welcome {user.get_full_name()}!"
        )

        return user

    

    def get_user(self, user_id, role=None):

        user_data = self.user_dao.get_user_by_id(user_id, role)

        if user_data is None:
            return None

        if user_data["role_name"] == "ADMIN":
            return Admin(
                user_id=user_data["user_id"],
                name=user_data["name"],
                email=user_data["email"]
            )

        return Customer(
            user_id=user_data["user_id"],
            name=user_data["name"],
            email=user_data["email"],
            contact_name=user_data["contact_name"],
            address=user_data["address"],
            city=user_data["city"],
            postal_code=user_data["postal_code"],
            country=user_data["country"]
        )

   

    def delete_account(self, email, password):

        email = email.strip().lower()

         

        user_data = self.user_dao.get_user_by_email(email)

        if user_data is None:
            print("User not found.")
            return False

        

        if not verify_password(
            password,
            user_data["password_hash"]
        ):
            print("Invalid password.")
            return False

        

        success = self.user_dao.delete_user(
            user_data["user_id"],
            user_data["role_name"]
        )

        if success:
            print("Account deleted successfully.")
            return True

        print("Failed to delete account.")
        return False