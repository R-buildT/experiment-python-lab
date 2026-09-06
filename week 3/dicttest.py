dict = {'prince':500,'RT':250,'ritam':450}

a = input('enter new name')
total = dict['prince']+dict['ritam']+dict['RT']
dict.setdefault(a,total)



print(dict)