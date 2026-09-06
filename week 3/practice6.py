sentence = 'hello nigga boy i wanted to say high to the nigga boy name lundveer licing near the citing of lundveer'
splited = sentence.split()
tu = {}
for i in splited:
    tu.setdefault(i,0)
    tu[i] += 1

print(tu)