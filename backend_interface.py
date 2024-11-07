import ctypes
import os

# Load the C library
lib = ctypes.CDLL(os.path.join(".", "libcalculations.so"))

# Define a dictionary to map operation names to their corresponding functions
operations = {
    'add': lib.add,
    'subtract': lib.subtract,
    'multiply': lib.multiply,
    'divide': lib.divide
}

# Define a function to perform an operation
def perform_operation(operation, a, b):
    if operation in operations:
        return operations[operation](ctypes.c_double(a), ctypes.c_double(b))
    else:
        raise ValueError("Invalid operation")

# Define Python-accessible functions
def add(a, b):
    return perform_operation('add', a, b)

def subtract(a, b):
    return perform_operation('subtract', a, b)

def multiply(a, b):
    return perform_operation('multiply', a, b)

def divide(a, b):
    return perform_operation('divide', a, b)