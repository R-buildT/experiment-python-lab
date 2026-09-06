birthdays =  {'ranveer':'aug 6','prince':'april 3','prity':'may 6'}

while True:
    name=input('enter name ')
    if name == '':
        break


    if name in birthdays:
        print('dict found')
        print(birthdays.get(name))
        break
    else:
        print("not found")
        bday = input("new data = ")

        birthdays.update({name:bday})
        print("updated dict succesfully")
        print(birthdays)
    
        