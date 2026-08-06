num1_str = input("Enter a number: ")
num2_str = input("Enter another number: ")
num3_str = input("Enter a third number: ")
operation = input("enter operation: ")

def calculate(num1_str, num2_str, num3_str, operation):
    try:
        if operation == '+':
            if num3_str == '':
                return int(num1_str) + int(num2_str)
            elif num2_str == '':
                return int(num1_str) + int(num3_str)
            elif num1_str == '':
                return int(num2_str) + int(num3_str)
            else:
                return int(num1_str) + int(num2_str) + int(num3_str)
        elif operation == '-':
            if num3_str == '':
                return int(num1_str) - int(num2_str)
            elif num2_str == '':
                return int(num1_str) - int(num3_str)
            elif num1_str == '':
                return int(num2_str) - int(num3_str)
            else:
                return int(num1_str) - int(num2_str) - int(num3_str)
        elif operation == '*':
            if num3_str == '':
                return int(num1_str) * int(num2_str)
            elif num2_str == '':
                return int(num1_str) * int(num3_str)
            elif num1_str == '':
                return int(num2_str) * int(num3_str)
            else:
                return int(num1_str) * int(num2_str) * int(num3_str)
        elif operation == '/':
            if num3_str == '':
                return int(num1_str) / int(num2_str)
            elif num2_str == '':
                return int(num1_str) / int(num3_str)
            elif num1_str == '':
                return int(num2_str) / int(num3_str)
        else:
            return 'invalid operation'
    except ValueError:
        return "invalid value"

print(calculate(num1_str, num2_str, num3_str, operation))
