a = (input('enter a no. = '))

try:
    if a == int(a):
        print ('number valid')

except ValueError:
    print('invalid response')