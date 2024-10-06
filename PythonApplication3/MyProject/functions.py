# functions.py

def greet():
    """Функция без параметров, приветствует пользователя."""
    return "Hello, User!"

def add(a, b):
    """Функция с параметрами, возвращает сумму двух чисел."""
    return a + b

def calculate_area(length=1, width=1):
    """Функция с несколькими параметрами, значения по умолчанию."""
    return length * width

def multiply(a: int, b: int) -> int:
    """Функция с заданным типом параметров."""
    return a * b

def combine_numbers(*args):
    """Функция с неопределённым количеством параметров."""
    return sum(args)

def print_info(**kwargs):
    """Функция с неопределённым количеством параметров (kwargs)."""
    return ', '.join(f"{key}: {value}" for key, value in kwargs.items())

def outer_function():
    """Функция, вызывающая внутри себя другую функцию."""
    
    def inner_function():
        return "Inner function called!"
    
    return inner_function()

def process_function(func):
    """Функция, принимающая функцию как параметр."""
    result = func(5)
    return f"Processed result: {result}"

# Примеры использования функций, принимающих функцию как параметр
def square(x):
    return x * x

def cube(x):
    return x * x * x

def execute_functions():
    return process_function(square), process_function(cube)

def main_function():
    """Функция с объявленной внутри локальной функцией."""
    def helper():
        return "Helper function in main_function!"
    
    return helper()

def another_main_function():
    """Ещё одна функция с локальной функцией."""
    def local_function():
        return "Local function inside another_main_function!"
    
    return local_function()

# Лямбда-выражения
lambda_no_params = lambda: "This is a lambda with no parameters."

lambda_with_params = lambda x, y: x + y

def use_lambda(func):
    """Функция, принимающая лямбда-выражение как параметр."""
    return f"Result of lambda: {func(3, 5)}"

def closure_example(value):
    """Функция с замыканиями."""
    def inner():
        return f"Closed value: {value}"
    
    return inner

# Другой пример замыкания
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Третий пример замыкания
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply
