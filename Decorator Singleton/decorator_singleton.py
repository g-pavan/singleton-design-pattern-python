# Decorator for Singleton Pattern
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

# Applying the Singleton Decorator
@singleton
class SingletonClass:
    def __init(self, data=None):
        self.data = data

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

# Example Usage
if __name__ == "__main__":
    # Creating instances of SingletonClass
    singleton1 = SingletonClass()
    singleton1.add_data("Data 1")

    # Accessing the same instance
    singleton2 = SingletonClass()

    # Both instances are the same
    print(singleton1 is singleton2)  # Output: True

    # Access the data from both instances
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    # Modify the data from both instances
    singleton2.add_data("Data 2")
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'
