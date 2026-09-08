try:
    while True:
        a = input("Enter a number: ")
        b = input("Enter another number: ")
        c = int(a)/int(b)
        print(c)
        
except ValueError:
    print('invalid value')

except ZeroDivisionError:
    print('division by 0 not allowed')