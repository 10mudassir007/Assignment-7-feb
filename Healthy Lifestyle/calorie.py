age = int(input('Enter your age : '))
weight = int(input('Enter your weight : '))
activity = input('Enter your activity level : ')

if activity == 'Little to no':
    print('Calories required daily:',1800)
elif activity == 'Moderate':
    print('Calories required daily:',2200)
elif activity == 'High intensity':
    print('Calories required daily:',2700)


