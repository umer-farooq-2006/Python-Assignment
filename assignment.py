# 1. Numeric Data Types

x: int = 10  # Integer
y: float = 10.5  # Float
print(type(x), type(y))

# 2. String Data Type

name: str = "Python Programming"
print(type(name))  # Output: <class 'str'>

# 3. Boolean Data Type

is_python_easy: bool = True
print(type(is_python_easy))  # Output: <class 'bool'>

# 4. Sequence Data Types

my_list: list = [1, 2, 3]  # List (mutable)
my_tuple: tuple = (10, 20, 30)  # Tuple (immutable)
print(type(my_list), type(my_tuple))

# 5. Dictionary (Mapping Type)

my_dict: dict = {"name": "Python", "version": 3.9}
print(my_dict["name"], my_dict["version"])  # Output: Python, 3.9

# 1. Function: Sum of Two Numbers

def add_numbers(a, b):
    return a + b

# Function Call
result = add_numbers(5, 10)
print("Sum:", result)  # Output: Sum: 15

# 2. Function: Check Even or Odd

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function Call
num = 7
print(f"{num} is", check_even_odd(num))  # Output: 7 is Odd