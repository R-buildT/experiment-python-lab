a = input("Enter a number: ")
b = input("Enter another number: ")
c = input("Enter a third number: ")
d = input("enter operation: ")
def func(a,b,c):
    try:
        if d == '+':
            if c == '':
                return int(a) + int(b)
            elif b == '':
                return int(a) + int(c)
            elif a == '':
                return int(b) + int(c)
            else:
                return int(a) + int(b) + int(c)
        elif d == '-':
            if c == '':
                return int(a) - int(b)
            elif b == '':
                return int(a) - int(c)
            elif a == '':
                return int(b) - int(c)
            else:
                return int(a) - int(b) - int(c)
        elif d == '*':
            if c == '':
                return int(a) * int(b)
            elif b == '':
                return int(a) * int(c)
            elif a == '':
                return int(b) * int(c)
            else:
                return int(a) * int(b) * int(c)
        elif d == ('/'):
            if c == '':
                return int(a)/int(b)
            elif b == '':
                return int(a)/int(c)
            elif a == '':
                return int(b)/int(c)
        else:
            return('invalid operation')
    except ValueError:
        return "invalid value"

print(func(a,b,c))