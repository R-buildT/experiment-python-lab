sentence = 'hello nigga boy i wanted to say high to the nigga boy name lundveer licing near the citing of lundveer'
splited = sentence.split()
my_dict = {}

for i in splited:
    my_dict.setdefault(i,0)
    my_dict[i] += 1

print(my_dict)