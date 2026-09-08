while True:
    print('enter you adhaar id no. ')
    num = input('==> ')
    if num.isdecimal():
        print("no. succesfully entered")
        break
    print('we only accept numbers')