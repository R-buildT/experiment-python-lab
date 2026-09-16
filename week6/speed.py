a = 0
for i in range(0,100000000):
    a = i
    if i % 10000000 == 0:
        print(f"Current: {a}")

print(f"Done! Final: {a}")