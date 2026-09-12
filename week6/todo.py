print('''enter your work down below
    \\/
    \\/''')
work=[]
a=input('\n >>>').lower()
work.append(a)
while True:
    print('want to add more??')
    if input().lower()=='yes':
        print('enter another task')
        b=input('>').lower()
        work.append(b)
    else:
        break
print(work)