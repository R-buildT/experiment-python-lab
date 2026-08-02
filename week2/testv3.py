message = input()
bu = {}
for i in message:
    bu.setdefault(i,0)
    bu[i] = bu[i]+1

print(bu)