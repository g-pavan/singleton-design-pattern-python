class ClassicSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClassicSingleton, cls).__new__(cls)
            cls._instance.data = None  # Initialize the data attribute
        return cls._instance

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

# Example usage of the Classic Singleton pattern
if __name__ == "__main__":
    # Creating an instance of the Classic Singleton
    singleton1 = ClassicSingleton()
    singleton1.add_data("Data 1")

    # Accessing the same instance
    singleton2 = ClassicSingleton()

    # Both instances are the same
    print(singleton1 is singleton2)  # Output: True
    
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    singleton2.add_data("Data 2")
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'
