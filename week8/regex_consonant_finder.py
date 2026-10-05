import re
import time

text='''hello The method call match.group() returns the full matched text 'Catch', while match.group(1) returns just the part of the matched text 
inside the first parentheses group, 
'ch'. By using the pipe 
character and grouping parentheses, you can specify several alternative patterns you 
would like your regex to match. 
bro how  hand??'''
pattern=r'[^aeiou]'

finding=re.finditer(pattern,text)

for p, i in enumerate(finding):
    time.sleep(0.01)
    print([p],i.group(),i.span())
