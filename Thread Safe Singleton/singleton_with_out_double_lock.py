class SingletonWithOutDoubleLock:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonWithOutDoubleLock, cls).__new__(cls)
        return cls._instance

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

if __name__ == "__main__":
    # Create instances of the Singleton class without passing data
    singleton1 = SingletonWithOutDoubleLock()
    singleton1.add_data("Data 1")

    # Accessing the same instance
    singleton2 = SingletonWithOutDoubleLock()

    # Both instances are the same
    print(singleton1 is singleton2)  # Output: True

    # Access the data from both instances
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    # Modify the data from both instances
    singleton2.add_data("Data 2")
    
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'