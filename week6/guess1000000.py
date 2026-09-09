import random

counts = {'Head': 0, 'Tails': 0}

for _ in range(10000000):
    result = random.choice(['Head', 'Tails'])
    if result == 'Head':
        counts['Head'] += 1
    else:
        counts['Tails'] += 1


print(counts)