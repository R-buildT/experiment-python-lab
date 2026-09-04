guest = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num = 0
    for person, brought_items in guests.items():
        num = num + brought_items.get(item, 0)
    return num

print('- apples ' + str(total_brought(guest,'apples')))
