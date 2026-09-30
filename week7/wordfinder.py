import re

print('''_____________________________________
 ENTER YOUR TEXT YOUR WANT TO SEARCH''')

a=input('>> ')
print('''_______________________________________
 PASTE YOUR TEXT YOU WANT TO SEARCH IN''')
text=(input('>>'))
finding=re.finditer(a,text)
for index, i in enumerate(finding):
    coordinate=i.span()
    word=i.group()
    print([index+1],word,coordinate)
