def birthdaystore():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('Enter a name: (blank to quit)')
        name=input()

        if name=='':
            break
        
        if name in birthdays:
            print(f'{birthdays[name]} is the birthday of {name}')
        else:
            print(f'I dont have data for {name}')
            print('when is his/her birthday?')
            day=input()
            birthdays[name]=day
            print('birthdays have been updated!')

birthdaystore()
