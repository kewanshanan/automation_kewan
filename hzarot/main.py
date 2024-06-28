from calc import Calculator


def main():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            sum_numbers = Calculator.add(a, b)
            print(f"The sum of {a} and {b} is : {sum_numbers}")

            subtract_numbers = Calculator.subtract(a, b)
            print(f"The difference of {a} and {b} is : {subtract_numbers}")

            multiply_numbers = Calculator.multiply(a, b)
            print(f"The multiplication of {a} and {b} is : {multiply_numbers}")

            divide_numbers = Calculator.divide(a, b)
            print(f"The division of {a} and {b} is : {divide_numbers}")

            power_numbers = Calculator.power(a, b)
            print(f"The power of {a} and {b} is : {power_numbers}")

            square_numbers = Calculator.square(a, b)
            print(f"The square of {a} and {b} is : {square_numbers}")

        except ValueError as e:
            print(e)
        new_input = input("if you want to continue, type 'y' to continue, if you want to exit, type 'q' to quit: ")
        if new_input == 'y':
            continue
        elif new_input == 'q':
            break


if __name__ == '__main__':
    main()
