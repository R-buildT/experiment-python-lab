def func(abc):
    try:
        return 999 / abc
    except ZeroDivisionError:
        return "error while doing operation"


print(func(45))
print(func(99))
print(func(0))
print(func(2))

#try: and except: are used to handle exceptions in Python. In this code, the function func takes an 
# argument abc and attempts to divide 999 by abc. If abc is zero, a ZeroDivisionError will occur, and the 
# except block will catch that error and return a custom error message instead of crashing the program.