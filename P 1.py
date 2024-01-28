# Mixin for Logging
class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

# Mixin for Serialization
class SerializationMixin:
    def serialize(self):
        # Placeholder serialization logic
        return f"Serialized: {vars(self)}"

# Class using Mixins
class MyEnhancedClass(LoggingMixin, SerializationMixin):
    def __init__(self, name):
        self.name = name

# Example usage:
obj = MyEnhancedClass("Example")
obj.log("This is a log message.")
serialized_data = obj.serialize()
print(serialized_data)
