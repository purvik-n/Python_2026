
# ============================================================
# Advanced Python - Descriptors
# ============================================================
# Descriptors define how attribute access (get/set/delete) is
# handled. They power Python's property, classmethod, staticmethod.

# ------ 1. Data Descriptor (implements __set__) ------
class Validated:
    """A descriptor that validates its value before storing."""

    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:   # accessed on the class, not an instance
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    def validate(self, value):
        pass   # override in subclasses


class PositiveNumber(Validated):
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected a number, got {type(value)}")
        if value <= 0:
            raise ValueError(f"Expected a positive number, got {value}")


class NonEmptyString(Validated):
    def validate(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Must be a non-empty string.")


# ------ 2. Using Descriptors in a Class ------
class Product:
    name  = NonEmptyString()
    price = PositiveNumber()
    stock = PositiveNumber()

    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.name!r}, price={self.price}, stock={self.stock})"


p = Product("Laptop", 999.99, 50)
print(p)

try:
    p.price = -5
except ValueError as e:
    print(f"Caught: {e}")

try:
    p.name = ""
except ValueError as e:
    print(f"Caught: {e}")


# ------ 3. Lazy Property Descriptor (Non-data) ------
class lazy_property:
    """Compute the value once and cache it on the instance."""
    def __init__(self, func):
        self.func = func
        self.attrname = None

    def __set_name__(self, owner, name):
        self.attrname = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        val = self.func(obj)
        # Store on instance dict, shadowing the descriptor
        obj.__dict__[self.attrname] = val
        return val


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazy_property
    def area(self):
        import math
        print("Computing area…")
        return math.pi * self.radius ** 2


c = Circle(5)
print(c.area)   # "Computing area…" then value
print(c.area)   # cached – no recomputation
