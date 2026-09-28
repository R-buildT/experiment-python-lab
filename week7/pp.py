import re

text='hkz pc shit hi'

a=re.finditer(r'i',text)

for i in a:
    print(i.group(),i.span())



