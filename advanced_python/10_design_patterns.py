
# ============================================================
# Advanced Python - Design Patterns
# ============================================================
# Design patterns are reusable solutions to common problems.
# This file covers: Singleton, Factory, Observer, Strategy,
# and Command patterns in idiomatic Python.


# ------ 1. Singleton (thread-safe) ------
import threading

class _SingletonMeta(type):
    _instances: dict = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=_SingletonMeta):
    def __init__(self):
        self.debug = False
        self.db_url = "sqlite:///app.db"


cfg1 = AppConfig()
cfg2 = AppConfig()
assert cfg1 is cfg2
print("Singleton OK:", cfg1 is cfg2)


# ------ 2. Factory Pattern ------
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...


class EmailNotification(Notification):
    def __init__(self, address: str):
        self.address = address
    def send(self, message: str) -> None:
        print(f"Email → {self.address}: {message}")


class SMSNotification(Notification):
    def __init__(self, phone: str):
        self.phone = phone
    def send(self, message: str) -> None:
        print(f"SMS  → {self.phone}: {message}")


class PushNotification(Notification):
    def __init__(self, token: str):
        self.token = token
    def send(self, message: str) -> None:
        print(f"Push → {self.token}: {message}")


def notification_factory(kind: str, **kwargs) -> Notification:
    registry = {
        "email": EmailNotification,
        "sms":   SMSNotification,
        "push":  PushNotification,
    }
    cls = registry.get(kind)
    if not cls:
        raise ValueError(f"Unknown notification type: {kind!r}")
    return cls(**kwargs)


n = notification_factory("email", address="user@example.com")
n.send("Your order shipped!")


# ------ 3. Observer Pattern ------
from typing import Callable

class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, list[Callable]] = {}

    def on(self, event: str, callback: Callable) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event: str, *args, **kwargs) -> None:
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


bus = EventEmitter()
bus.on("login", lambda user: print(f"Audit: {user} logged in"))
bus.on("login", lambda user: print(f"Email: Welcome back, {user}!"))
bus.emit("login", "purvik")


# ------ 4. Strategy Pattern ------
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, data: list) -> list: ...


class BubbleSort:
    def sort(self, data: list) -> list:
        d = list(data)
        for i in range(len(d)):
            for j in range(len(d) - i - 1):
                if d[j] > d[j + 1]:
                    d[j], d[j + 1] = d[j + 1], d[j]
        return d


class QuickSort:
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left  = [x for x in data if x < pivot]
        mid   = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data: list) -> list:
        return self.strategy.sort(data)


data = [5, 3, 8, 1, 9, 2]
print(Sorter(QuickSort()).sort(data))
print(Sorter(BubbleSort()).sort(data))


# ------ 5. Command Pattern ------
class Command(Protocol):
    def execute(self) -> None: ...
    def undo(self) -> None: ...


class TextEditor:
    def __init__(self):
        self.content = ""
        self._history: list[Command] = []

    def execute(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)

    def undo(self) -> None:
        if self._history:
            self._history.pop().undo()


class InsertText:
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.content += self.text

    def undo(self):
        self.editor.content = self.editor.content[: -len(self.text)]


ed = TextEditor()
ed.execute(InsertText(ed, "Hello"))
ed.execute(InsertText(ed, ", World"))
print(ed.content)   # Hello, World
ed.undo()
print(ed.content)   # Hello
