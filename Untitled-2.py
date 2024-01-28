class CustomLogicMeta(type):
    def __init__(cls, name, bases, attrs):
        # Inject custom logic during class creation
        print(f"Custom logic executed for class: {name}")
        super().__init__(name, bases, attrs)

# Example usage:
class MyClass(metaclass=CustomLogicMeta):
    def my_method(self):
        pass
