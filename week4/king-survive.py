import random

king = 'R-T'
work = 'LORD'
place = 'pyland'

print(f'welcome the {work} {place} our majesty {king}')
a = random.randint(1,20)
c = random.randint(1,20)
print(f'do you want to predict {work}\'s death')
b = input('>>')

if b == 'yes':
    if  a == c:
        print(f'thank you for your service {work} \n {work} died on', a ,'years after appointment')
    else:
        print(f'{work} gets to see another day')
    