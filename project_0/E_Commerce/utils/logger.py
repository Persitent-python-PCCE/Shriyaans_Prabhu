import csv
import json
from datetime import datetime, timezone
from pathlib import Path


class AppLogger:
    """Simple file-based logger and backup utility for JSON/CSV data."""

    def __init__(self, base_dir=None, log_dir="logs", backup_dir="backups"):
        if base_dir is None:
            base_dir = Path(__file__).resolve().parent.parent
        else:
            base_dir = Path(base_dir)

        self.base_dir = base_dir
        self.log_dir = base_dir / log_dir
        self.backup_dir = base_dir / backup_dir
        self._ensure_directories()

    def _ensure_directories(self):
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def _timestamp(self):
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    def _read_json_file(self, file_path):
        if not file_path.exists():
            return []

        try:
            content = file_path.read_text(encoding="utf-8")
            if not content.strip():
                return []
            data = json.loads(content)
            return data if isinstance(data, list) else [data]
        except (json.JSONDecodeError, OSError):
            return []

    def log_event(self, event_type, message, details=None, level="INFO"):
        """Append a structured event to a JSON log file."""
        if details is None:
            details = {}

        entry = {
            "timestamp": self._timestamp(),
            "level": str(level).upper(),
            "event_type": str(event_type),
            "message": str(message),
            "details": details,
        }

        log_file = self.log_dir / "app_log.json"
        entries = self._read_json_file(log_file)
        entries.append(entry)
        log_file.write_text(json.dumps(entries, indent=2), encoding="utf-8")
        return entry

    def backup_data(self, name, data, file_format="json"):
        """Create a CSV or JSON backup file from a list of dictionaries."""
        normalized_name = str(name).strip()
        if not normalized_name:
            raise ValueError("Backup name cannot be empty.")

        file_format = str(file_format).lower()
        if file_format == "json":
            destination = self.backup_dir / f"{normalized_name}.json"
            payload = data if isinstance(data, list) else [data]
            destination.write_text(
                json.dumps(payload, indent=2, default=str),
                encoding="utf-8",
            )
            self.log_event(
                event_type="DATA_BACKUP",
                message=f"Backup created: {normalized_name}.json",
                details={"file": str(destination), "format": "json"},
            )
            return destination

        if file_format == "csv":
            if not isinstance(data, list) or not data:
                rows = []
            else:
                rows = data

            destination = self.backup_dir / f"{normalized_name}.csv"
            fieldnames = []
            for row in rows:
                if isinstance(row, dict):
                    for key in row.keys():
                        if key not in fieldnames:
                            fieldnames.append(key)

            with destination.open("w", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                if fieldnames:
                    writer.writeheader()
                    for row in rows:
                        writer.writerow({key: row.get(key, "") for key in fieldnames})

            self.log_event(
                event_type="DATA_BACKUP",
                message=f"Backup created: {normalized_name}.csv",
                details={"file": str(destination), "format": "csv"},
            )
            return destination

        raise ValueError("Unsupported backup format. Use 'json' or 'csv'.")


logger = AppLogger()
