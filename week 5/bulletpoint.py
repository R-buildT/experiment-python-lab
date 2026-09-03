
text = 'Lists of animals \nLists of aquarium life \nLists of biologists by author abbreviation \nLists of cultivars'
line = text.split('\n')

for c in range(len(line)):
    line[c] = 'X ' + line[c]

alt_text = '\n'.join(line)

print(alt_text)