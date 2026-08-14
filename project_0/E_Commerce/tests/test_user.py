# from unittest.mock import Mock, patch
from service.user_service import UserService
def login_valid(monkeypatch):
    service=UserService()
    user_data = {
        "user_id": 1,
        "role_name": "CUSTOMER",
        "name": "Test User",
        "email": "test@example.com",
        "password_hash": "hashed_password",
        "contact_name": None,
        "address": None,
        "city": None,
        "postal_code": None,
        "country": None
    }
    monkeypatch.setattr(service.user_dao,"get_user_name",lambda name:user_data)
    monkeypatch.setattr(service.user_dao,"service.user_service.verify_password",lambda password,hash_password:True)
    user=service.login("raj","user@1233")
    assert user is not None
    assert user.get_role()=="CUSTOMER"
    assert user.get_role()=="ADMIN"
    assert user.name=="raj"
def login_invalid(monkeypatch):
   service=UserService()
   monkeypatch.setattr(service.user_dao,"get_user_by_name",lambda name:None)
   user=service.login("anonyms","wrong@123")
   assert user is None
