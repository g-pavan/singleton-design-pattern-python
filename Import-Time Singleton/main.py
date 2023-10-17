# main.py
from singleton import singleton_instance

if __name__ == "__main__":
    # Access the Singleton instance
    singleton1 = singleton_instance
    singleton1.add_data("Data 1")

    # Attempt to create another instance (which will not work)
    try:
        new_singleton = Singleton("Data 2")
    except AttributeError:
        print("Creating a new instance is not allowed.")

    # Access the same instance
    singleton2 = singleton_instance
    print(singleton1 is singleton2)  # Output: True

    # Access and modify the data from both instances
    print(singleton1.get_data())  # Output: 'Data 1'
    print(singleton2.get_data())  # Output: 'Data 1'

    singleton2.add_data("Data 2")
    print(singleton1.get_data())  # Output: 'Data 2'
    print(singleton2.get_data())  # Output: 'Data 2'
