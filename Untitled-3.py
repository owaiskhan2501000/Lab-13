class AttributeValidationMeta(type):
    def __new__(cls, name, bases, attrs):
        # Perform custom validation on attributes
        for attr_name, value in attrs.items():
            if isinstance(value, int) and value < 0:
                raise ValueError(f"Attribute '{attr_name}' must be a non-negative integer.")

        return super().__new__(cls, name, bases, attrs)

# Example usage:
class MyClass(metaclass=AttributeValidationMeta):
    positive_number = 42  # Valid attribute
    negative_number = -5  # Raises ValueError during class creation
