from service.order_service import OrderService
def test_place_order(monkeypatch):

    service = OrderService()

    monkeypatch.setattr(
        service.order_dao,
        "create_order",
        lambda customer_id, items, status: 1001
    )

    monkeypatch.setattr(
        service.order_dao,
        "get_order_by_id",
        lambda order_id: {
            "order_id": 1001,
            "customer_id": 1,
            "order_date": "2026-08-14 19:00:00",
            "total_amount": 1000,
            "status": "PLACED"
        }
    )

    monkeypatch.setattr(
        service.order_dao,
        "get_order_details",
        lambda order_id: [
            {
                "order_detail_id": 1,
                "order_id": 1001,
                "product_id": 1,
                "product_name": "Book",
                "quantity": 2,
                "unit_price": 500
            }
        ]
    )

    order = service.place_order(
        customer_id=1,
        items=[
            {
                "product_id": 1,
                "quantity": 2
            }
        ]
    )

    assert order is not None
    assert order.order_id == 1001
    assert order.customer_id == 1
    assert order.status == "PLACED"


def test_empty_order():

    service = OrderService()

    order = service.place_order(
        customer_id=1,
        items=[]
    )

    assert order is None


def test_invalid_quantity():

    service = OrderService()

    order = service.place_order(
        customer_id=1,
        items=[
            {
                "product_id": 1,
                "quantity": 0
            }
        ]
    )

    assert order is None


def test_update_order_status(monkeypatch):

    service = OrderService()

    monkeypatch.setattr(
        service.order_dao,
        "get_order_by_id",
        lambda order_id: {
            "order_id": 1001,
            "customer_id": 1,
            "order_date": "2026-08-14 19:00:00",
            "total_amount": 1000,
            "status": "PLACED"
        }
    )

    monkeypatch.setattr(
        service.order_dao,
        "update_order_status",
        lambda order_id, status: True
    )

    result = service.update_order_status(
        order_id=1001,
        status="SHIPPED"
    )

    assert result is True


def test_invalid_order_status():

    service = OrderService()

    result = service.update_order_status(
        order_id=1001,
        status="INVALID"
    )

    assert result is False