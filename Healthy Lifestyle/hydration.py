x = int(input('Enter weight : '))
activity = input('Enter activity level : ')

if x > 60:
    if activity == 'Light':
        print('Water needed daily 3.5-4 liters')
    elif activity == 'Moderate':
        print('Water needed daily 4-5 liters')
    elif activity == 'High':
        print('Water needed daily 5-6 liters')
else:
    if activity == 'Light':
        print('Water needed daily 3-4 liters')
    elif activity == 'Moderate':
        print('Water needed daily 3.5-5 liters')
    elif activity == 'High':
        print('Water needed daily 4-6 liters')
    