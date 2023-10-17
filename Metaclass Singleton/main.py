class SingletonMeta(type):
    """
    Metaclass for implementing the Singleton pattern.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """
    Singleton class using the Metaclass Approach.
    """
    def __init__(self, data=None):
        self.data = data

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

if __name__ == "__main__":
    # Create instances of the Singleton class without passing data
    singleton1 = Singleton()
    singleton1.add_data("Data 1")

    # Accessing the same instance
    singleton2 = Singleton()

    # Both instances are the same
    print(singleton1 is singleton2)  # Output: True

    # Access the data from both instances
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    # Modify the data from both instances
    singleton2.add_data("Data 2")
    
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'
