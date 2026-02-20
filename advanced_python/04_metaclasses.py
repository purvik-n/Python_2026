
# ============================================================
# Advanced Python - Metaclasses
# ============================================================
# A metaclass is the "class of a class."
# Just as an object is created by a class, a class is created
# by a metaclass. The default metaclass is `type`.

# ------ 1. Everything is an object ------
print(type(42))        # <class 'int'>
print(type(int))       # <class 'type'>
print(type(type))      # <class 'type'>  (type is its own metaclass)


# ------ 2. Creating a class dynamically with type() ------
# type(name, bases, namespace)
Dog = type("Dog", (object,), {
    "species": "Canis familiaris",
    "bark": lambda self: f"{self.species} says: Woof!",
})

d = Dog()
print(d.bark())


# ------ 3. Custom Metaclass ------
class SingletonMeta(type):
    """Metaclass that ensures only one instance per class."""
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url


db1 = Database("postgres://localhost/mydb")
db2 = Database("postgres://localhost/other")
print(db1 is db2)       # True  – same object!
print(db1.url)          # postgres://localhost/mydb


# ------ 4. Metaclass for attribute validation ------
class ValidatedMeta(type):
    """Ensure all method names are lowercase."""
    def __new__(mcs, name, bases, namespace):
        for attr_name in namespace:
            if not attr_name.startswith("_") and not attr_name.islower():
                raise TypeError(
                    f"Method '{attr_name}' in class '{name}' must be lowercase."
                )
        return super().__new__(mcs, name, bases, namespace)


class MyService(metaclass=ValidatedMeta):
    def process_data(self):
        return "processing"

    def run(self):
        return "running"


# Uncommenting below would raise TypeError:
# class BadService(metaclass=ValidatedMeta):
#     def ProcessData(self):  # Capital letter!
#         pass


# ------ 5. __init_subclass__ – a lighter alternative ------
class PluginBase:
    _plugins: dict = {}

    def __init_subclass__(cls, plugin_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if plugin_name:
            PluginBase._plugins[plugin_name] = cls


class CSVPlugin(PluginBase, plugin_name="csv"):
    def load(self): return "loading csv"


class JSONPlugin(PluginBase, plugin_name="json"):
    def load(self): return "loading json"


print(PluginBase._plugins)
# {'csv': <class 'CSVPlugin'>, 'json': <class 'JSONPlugin'>}
