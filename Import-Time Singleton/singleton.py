# singleton.py

class Singleton:
    def __init__(self, data=None):
        self.data = data

    def add_data(self, item):
        self.data = item

    def get_data(self):
        return self.data

# Create the Singleton instance
singleton_instance = Singleton()
