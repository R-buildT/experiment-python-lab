my_dict = {'prince':500,'RT':250,'ritam':450}

a = input('enter new name')
total = my_dict['prince']+my_dict['ritam']+my_dict['RT']
my_dict.setdefault(a,total)



print(my_dict)