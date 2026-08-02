i = input()

dict = {}

for o in i:


    if o == " ":
        continue


    if o in dict:
        dict[o] += 1
    else:
        dict[o] =1

print(dict)