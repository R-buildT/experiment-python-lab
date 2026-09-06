def divide_numbers(divisor):
    """Divide 999 by the given divisor, handling division by zero errors."""
    try:
        return 999 / divisor
    except ZeroDivisionError:
        return "error while doing operation"

if __name__ == '__main__':
    print(divide_numbers(45))
    print(divide_numbers(99))
    print(divide_numbers(0))
    print(divide_numbers(2))
