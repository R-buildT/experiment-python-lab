num = [ 1,4,9,16,25,36,49,64,81,100]

o = 0

while o <= len(num)-1: 
    print(num[o])
    o += 1

num1 = [ 1,4,9,16,25,36,49,64,81,100]

x = 25

i = 0
while i < len(num1):
    if(num1[i] == x):
        print("found!! >> ", i)
        break
    else:
        print("Finding...")
    i += 1