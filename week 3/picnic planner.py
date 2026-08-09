guest = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(p,t):
    num = 0
    for v,k in p.items():
        num = num + k.get(t, 0)
    return num

print('- apples ' + str(total_brought(guest,'apples')))