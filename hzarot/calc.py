class Calculator:
    @staticmethod
    def add(a, b):
        try:
            return float(a + b)
        except TypeError:
            raise ValueError("Both arguments must be numbers")

    @staticmethod
    def subtract(a, b):
        try:
            return float(a - b)
        except TypeError:
            raise ValueError("Both arguments must be numbers")

    @staticmethod
    def multiply(a, b):
        try:
            return float(a * b)
        except TypeError:
            raise ValueError("Both arguments must be numbers")

    @staticmethod
    def divide(a, b):
        try:
            return float(a / b)
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except TypeError:
            raise ValueError("Both arguments must be numbers")

    @staticmethod
    def power(a, b):
        try:
            return float(a ** b)
        except TypeError:
            raise ValueError("Both arguments must be numbers")

    @staticmethod
    def square(a, b):
        try:
            return float(a ** 2), float(b ** 2)
        except TypeError:
            raise ValueError("The argument must be a number")



