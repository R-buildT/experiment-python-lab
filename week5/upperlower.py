import pyperclip
a = 'hello bro'
pyperclip.copy(a)
text = pyperclip.paste(a)

result = []
false = False

for c in text:
    if false:
        result.append(c.upper())
    else:
        result.append(c.lower())
        
    false = not false
final_text = ''.join(result)
pyperclip.copy(final_text)
print(final_text)