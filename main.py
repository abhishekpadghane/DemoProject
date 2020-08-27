# importing functionalities from src package
from src.functionalities import Calculator

# creating instance of class Calculator
calculator = Calculator()

# creating a infinite loop for repeating the actions
while True:
    # reading space separated numbers from console in integer format
    numbers_list = list(map(int, input('Enter two numbers: ').split(' ')))

    # reading the operation that needs to be performed
    operation = input('Enter the operation: ')

    # displaying results
    print(eval('calculator.{}({})'.format(operation, numbers_list)))
