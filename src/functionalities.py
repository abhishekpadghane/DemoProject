# creating a class calculator
class Calculator:
    """
    This class holds functionality to perform arithmetic calculations

    Class/Static methods:

        add
        subtract
        mul
        float_division
        integer_division
    """

    # method for additions
    @staticmethod
    def add(*args):
        """
        This method adds two numbers and returns added value
        :param args: *args -> tuple -> int
        :return: addition -> int
        """
        return args[0] + args[1]

    # method for subtraction
    @staticmethod
    def subtract(*args):
        """
        This method subtract two numbers and returns there subtracted value
        :param args: *args -> tuple -> int
        :return: subtraction -> int
        """
        return args[0] - args[1]

    # method for multiplication
    @staticmethod
    def mul(*args):
        """
        This method multiplies two numbers and returns there product
        :param args: *args -> tuple -> int
        :return: product -> int
        """
        return args[0] * args[1]

    # method for float division
    @staticmethod
    def float_division(*args):
        return args[0] / args[1]

    # method for integer division
    @staticmethod
    def integer_division(*args):
        return args[0] // args[1]

    # method for getting remainder
    @staticmethod
    def float_modulus(*args):
        return args[0] % args[1]

    # method for getting power
    @staticmethod
    def power(number1, number2):
        return number1 ** number2

    # method for summation
    @staticmethod
    def sum(*args):
        sum = 0
        for number in args:
            sum += number
        return
