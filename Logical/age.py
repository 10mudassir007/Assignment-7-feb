age = int(input('Enter age : '))

if age < 13:
    print('You are a child')
elif age >= 13 and age < 18:
    print('You are a teenager')
elif age >= 18 and age < 60:
    print('You are a adult')
else:
    print('You are senior citizen')
    