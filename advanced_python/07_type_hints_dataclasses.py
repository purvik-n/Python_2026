
# ============================================================
# Advanced Python - Type Hints & dataclasses
# ============================================================
# Type hints (PEP 484) make code self-documenting and enable
# static analysis tools like mypy, pyright, and ruff.
# dataclasses (PEP 557) auto-generate boilerplate methods.

from __future__ import annotations
from dataclasses import dataclass, field, KW_ONLY
from typing import (
    Optional, Union, Literal, TypeVar, Generic,
    Callable, Any, overload, Protocol, runtime_checkable
)
import sys

# ------ 1. Basic Type Hints ------
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

print(greet("Purvik", 3))


# ------ 2. Generics ------
T = TypeVar("T")

def first(items: list[T]) -> T:
    if not items:
        raise IndexError("Empty list")
    return items[0]

print(first([10, 20, 30]))   # int
print(first(["a", "b"]))    # str


# ------ 3. Protocol (Structural Subtyping) ------
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str: return "○"

class Square:
    def draw(self) -> str: return "□"

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())
render(Square())
print(isinstance(Circle(), Drawable))   # True at runtime


# ------ 4. dataclass basics ------
@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p1 = Point(3.0, 4.0)
p2 = Point(0.0, 0.0)
print(p1.distance_to_origin())   # 5.0
print(sorted([p1, p2]))          # [Point(0.0, 0.0), Point(3.0, 4.0)]


# ------ 5. dataclass with defaults and post_init ------
@dataclass
class Employee:
    name: str
    department: str
    _: KW_ONLY            # everything after here is keyword-only
    salary: float = 50_000.0
    skills: list[str] = field(default_factory=list)
    _id: int = field(init=False)   # computed, not from constructor

    def __post_init__(self):
        import hashlib
        self._id = int(hashlib.md5(self.name.encode()).hexdigest(), 16) % 10**6
        self.name = self.name.title()

    def give_raise(self, percent: float) -> None:
        self.salary *= (1 + percent / 100)


emp = Employee("purvik gowda", "Engineering", salary=80_000, skills=["Python", "ML"])
print(emp)
emp.give_raise(10)
print(f"New salary: {emp.salary:,.2f}")


# ------ 6. Literal & overload ------
Mode = Literal["r", "w", "a", "rb", "wb"]

@overload
def open_file(path: str, mode: Literal["r"]) -> str: ...
@overload
def open_file(path: str, mode: Literal["rb"]) -> bytes: ...
def open_file(path: str, mode: Mode) -> str | bytes:
    with open(path, mode) as f:
        return f.read()
