import re

a=re.compile('hello friend')
b=a.search('hello friend and family today me and my daughter are going to present a talking monkey!! say hi to this wonderfull animal')

if b:
    print(b.group(),b.span())