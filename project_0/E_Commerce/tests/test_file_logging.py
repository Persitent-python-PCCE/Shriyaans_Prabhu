import json

from utils.logger import AppLogger


def test_log_event_writes_json_entry(tmp_path):
    logger = AppLogger(base_dir=str(tmp_path))

    entry = logger.log_event(
        event_type="USER_LOGIN",
        message="User logged in",
        details={"user_id": 1, "username": "alice"},
    )

    assert entry["event_type"] == "USER_LOGIN"
    assert entry["message"] == "User logged in"

    log_file = tmp_path / "logs" / "app_log.json"
    assert log_file.exists()

    content = json.loads(log_file.read_text())
    assert content[-1]["event_type"] == "USER_LOGIN"


def test_backup_data_writes_csv(tmp_path):
    logger = AppLogger(base_dir=str(tmp_path))

    rows = [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Phone", "price": 25000},
    ]

    csv_path = logger.backup_data(
        name="products",
        data=rows,
        file_format="csv",
    )

    assert csv_path.exists()
    content = csv_path.read_text()
    assert "id,name,price" in content
    assert "Laptop" in content
    assert "Phone" in content
