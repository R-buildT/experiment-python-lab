import re

text='hi man.This is a test text for my regex module'

hp=re.finditer('a',text)


for i in hp:
    print(i.group(),i.span())