# Singleton Design Pattern Implementations in Python

This repository contains various implementations of the Singleton design pattern in Python. The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. Each implementation is organized into separate folders and showcases a different approach to achieving this pattern.

## Implementations

### Classic Singleton

The Classic Singleton is one of the simplest and most straightforward ways to implement the Singleton pattern. It involves using a class-level attribute to maintain a single instance of the class. This approach provides basic Singleton behavior but does not offer thread safety.

**Usage:**
- [classic_singleton](classic_singleton/)

### Decorator Singleton

The Decorator Singleton is a creative way to implement the Singleton pattern. It leverages Python decorators to ensure that only one instance of a class is created. This approach is elegant and efficient, providing Singleton behavior while allowing easy customization of class instances.

**Usage:**
- [decorator_singleton](decorator_singleton/)

### Import-Time Singleton

The Import-Time Singleton utilizes Python's module-level code execution to create a Singleton instance when a module is imported for the first time. This is a simple approach that provides Singleton behavior but may not be suitable for all use cases.

**Usage:**
- [import_time_singleton](import_time_singleton/)

### Metaclass Singleton

The Metaclass Singleton is a powerful and advanced approach to implement the Singleton pattern. It uses metaclasses to enforce the Singleton behavior for classes. This approach offers flexibility and customization while maintaining a single instance.

**Usage:**
- [metaclass_singleton](metaclass_singleton/)

### Thread-Safe Singleton

The Thread-Safe Singleton is focused on ensuring thread safety in a multi-threaded environment. It provides both single locking and double-checked locking implementations to safeguard against issues in multi-threaded applications.

**Usage:**
- [singleton_with_double_lock](singleton_with_double_lock/)
- [singleton_without_double_lock](singleton_without_double_lock/)

## Usage

To use any of these Singleton implementations, navigate to the respective folder for the implementation you want to use. Inside each folder, you can follow the example usage provided in the Python script. Make sure to import the module for the desired Singleton implementation and create instances as demonstrated in the code examples.

## Contribute

Feel free to contribute to this repository by adding new Singleton implementations, improving existing ones, or providing better documentation within the individual implementation folders. If you find any issues or have suggestions, please create an issue or pull request.