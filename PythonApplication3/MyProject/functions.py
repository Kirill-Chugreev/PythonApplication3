# functions.py

def greet():
    """������� ��� ����������, ������������ ������������."""
    return "Hello, User!"

def add(a, b):
    """������� � �����������, ���������� ����� ���� �����."""
    return a + b

def calculate_area(length=1, width=1):
    """������� � ����������� �����������, �������� �� ���������."""
    return length * width

def multiply(a: int, b: int) -> int:
    """������� � �������� ����� ����������."""
    return a * b

def combine_numbers(*args):
    """������� � ������������� ����������� ����������."""
    return sum(args)

def print_info(**kwargs):
    """������� � ������������� ����������� ���������� (kwargs)."""
    return ', '.join(f"{key}: {value}" for key, value in kwargs.items())

def outer_function():
    """�������, ���������� ������ ���� ������ �������."""
    
    def inner_function():
        return "Inner function called!"
    
    return inner_function()

def process_function(func):
    """�������, ����������� ������� ��� ��������."""
    result = func(5)
    return f"Processed result: {result}"

# ������� ������������� �������, ����������� ������� ��� ��������
def square(x):
    return x * x

def cube(x):
    return x * x * x

def execute_functions():
    return process_function(square), process_function(cube)

def main_function():
    """������� � ����������� ������ ��������� ��������."""
    def helper():
        return "Helper function in main_function!"
    
    return helper()

def another_main_function():
    """��� ���� ������� � ��������� ��������."""
    def local_function():
        return "Local function inside another_main_function!"
    
    return local_function()

# ������-���������
lambda_no_params = lambda: "This is a lambda with no parameters."

lambda_with_params = lambda x, y: x + y

def use_lambda(func):
    """�������, ����������� ������-��������� ��� ��������."""
    return f"Result of lambda: {func(3, 5)}"

def closure_example(value):
    """������� � �����������."""
    def inner():
        return f"Closed value: {value}"
    
    return inner

# ������ ������ ���������
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# ������ ������ ���������
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
