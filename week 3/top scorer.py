def func():
    a = input('enter your name ')
    b = int(input('enter your no. '))
    return a, b

dictornary = {}

while True:
    key, value = func()
    dictornary[key] = value
    if input("do you want to continue? (y/n) ") == "n":
        break


best = None

max_score =  0

for name,score in dictornary.items():
    if score > max_score:
        max_score = score
        best = name

print(f"{max_score} scored by {best}")