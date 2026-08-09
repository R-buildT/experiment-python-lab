message = input("write a sentence: ")
tu = {}
for i in message:
  tu[i] = tu.get(i, 0) +1
print(tu)