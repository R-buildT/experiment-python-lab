inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
def func():
    while True:
        a = input('enter item name ')
        b = int(input('enter item quantity'))
        inventory[a] = b
        if input('yes/no') == 'no':
            break
func()
def total_items(i):
    total = 0
    for _, v in i.items():
        total = total + v
    return total

def show(inv):
    for amount in inv.values():
        print(amount)

print(total_items(inventory))

