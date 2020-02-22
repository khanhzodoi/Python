
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}


while True:
    name = str(input("Enter a name: (blank to quit): \n"))
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        bday = input('What is their birthday?\n')
        birthdays[name] = bday
        print('Birthday database updated.')
