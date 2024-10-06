# main.py

from functions import *

if __name__ == "__main__":
    print(greet())
    print(add(5, 7))
    print(calculate_area())
    print(multiply(4, 5))
    print(combine_numbers(1, 2, 3, 4, 5))
    print(print_info(name="Alice", age=30))
    
    print(outer_function())
    
    square_result, cube_result = execute_functions()
    print(square_result)
    print(cube_result)

    print(main_function())
    print(another_main_function())
    
    # Лямбда-выражения
    print(lambda_no_params())
    print(lambda_with_params(2, 3))
    print(use_lambda(lambda x, y: x - y))
    
    # Примеры замыканий
    closed_function = closure_example("Testing closure!")
    print(closed_function())

    increment_counter = counter()
    print(increment_counter())
    print(increment_counter())
    
    multiplier_by_2 = make_multiplier(2)
    print(multiplier_by_2(5))
