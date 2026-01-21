# Calculator

# Tasks:

# 1. Add a calculator logo
from calculator_art import logo

# 2. Add a additon feature to the calcualtor
from add import add

# 3. Add a subtraction feature to the calculator
from subtract import subtract

# 4. Add a multiplication feature to the calculator
from multiply import multiply

# 5. Add a division feature to the calculator
from divide import division

operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : division,
        }


def calculator():
    
    print(logo)
    
    num1 = float( input("What's the first number?: "))
    
    end_calculation = False
    
    while not end_calculation:
        
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num_2 = float( input("What's the next number?: "))
            
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num_2)
    
        print(f"{num1} {operation_symbol} {num_2} = {answer}")
            
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        
        if should_continue == 'y':
            num1 = answer
            
        if should_continue == 'n':
            end_calculation = True
            calculator()


calculator()