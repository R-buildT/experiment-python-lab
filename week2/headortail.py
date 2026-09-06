import random

storage = {
    'o': 0,
    'g': 0,
    'sequence': []
}

for i in range(100):
    flip = 'o' if random.randint(0, 1) == 0 else 'g'
    storage[flip] += 1
    storage['sequence'].append(flip)

print(' '.join(storage['sequence']))
print(storage)
