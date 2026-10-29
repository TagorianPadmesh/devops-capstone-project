"""Simple in-memory account model for an educational starter."""
from dataclasses import dataclass, asdict
from threading import Lock


@dataclass
class Account:
    """Customer account data."""
    name: str
    email: str
    address: str
    id: int | None = None

    def serialize(self):
        """Return a JSON-friendly representation."""
        return asdict(self)


class AccountStore:
    """Thread-safe in-memory store; replace with the course database model as needed."""
    def __init__(self):
        self._items = {}
        self._next_id = 1
        self._lock = Lock()

    def clear(self):
        with self._lock:
            self._items.clear()
            self._next_id = 1

    def create(self, data):
        with self._lock:
            account = Account(
                name=str(data.get("name", "")).strip(),
                email=str(data.get("email", "")).strip(),
                address=str(data.get("address", "")).strip(),
                id=self._next_id,
            )
            self._items[self._next_id] = account
            self._next_id += 1
            return account

    def all(self):
        with self._lock:
            return list(self._items.values())

    def find(self, account_id):
        with self._lock:
            return self._items.get(account_id)

    def update(self, account_id, data):
        with self._lock:
            account = self._items.get(account_id)
            if account is None:
                return None
            for field in ("name", "email", "address"):
                if field in data:
                    setattr(account, field, str(data[field]).strip())
            return account

    def delete(self, account_id):
        with self._lock:
            return self._items.pop(account_id, None)


store = AccountStore()
