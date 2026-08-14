from service.cart_service import CartService


def test_empty_cart(monkeypatch):

    service = CartService()

    monkeypatch.setattr(
        service.cart_dao,
        "get_cart",
        lambda customer_id: []
    )

    cart = service.get_cart(1)

    assert cart.items == []


def test_add_product_to_cart(monkeypatch):

    service = CartService()

    product = {
        "product_id": 1,
        "product_name": "Laptop",
        "price": 50000,
        "stock": 10
    }

    monkeypatch.setattr(
        service.product_dao,
        "get_product_by_id",
        lambda product_id: product
    )

    monkeypatch.setattr(
        service.cart_dao,
        "get_cart_item",
        lambda customer_id, product_id: None
    )

    def add_item(customer_id, product_id, quantity):
        return True

    monkeypatch.setattr(
        service.cart_dao,
        "add_item",
        add_item
    )

    result = service.add_item(
        customer_id=1,
        product_id=1,
        quantity=2
    )

    assert result is True


def test_remove_product_from_cart(monkeypatch):

    service = CartService()

    monkeypatch.setattr(
        service.cart_dao,
        "remove_item",
        lambda customer_id, product_id: True
    )

    result = service.remove_item(
        customer_id=1,
        product_id=1
    )

    assert result is True


def test_insufficient_stock(monkeypatch):

    service = CartService()

    product = {
        "product_id": 1,
        "product_name": "Laptop",
        "price": 50000,
        "stock": 3
    }

    monkeypatch.setattr(
        service.product_dao,
        "get_product_by_id",
        lambda product_id: product
    )

    monkeypatch.setattr(
        service.cart_dao,
        "get_cart_item",
        lambda customer_id, product_id: {
            "cart_id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 2
        }
    )

    def add_item(customer_id, product_id, quantity):
        return True

    monkeypatch.setattr(
        service.cart_dao,
        "add_item",
        add_item
    )

    result = service.add_item(
        customer_id=1,
        product_id=1,
        quantity=2
    )

    assert result is False


def test_update_cart_quantity(monkeypatch):

    service = CartService()

    product = {
        "product_id": 1,
        "product_name": "Laptop",
        "price": 50000,
        "stock": 10
    }

    monkeypatch.setattr(
        service.product_dao,
        "get_product_by_id",
        lambda product_id: product
    )

    monkeypatch.setattr(
        service.cart_dao,
        "get_cart_item",
        lambda customer_id, product_id: {
            "cart_id": 1,
            "customer_id": 1,
            "product_id": 1,
            "quantity": 2
        }
    )

    monkeypatch.setattr(
        service.cart_dao,
        "update_item",
        lambda customer_id, product_id, quantity: True
    )

    result = service.update_item(
        customer_id=1,
        product_id=1,
        quantity=5
    )

    assert result is True