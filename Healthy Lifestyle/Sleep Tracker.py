x = int(input('Enter bedtime(hours) : '))
y = int(input('Enter waking up time(hours) : '))

if x <= y:
    t_sleep = y - x
else:
    t_sleep = 24 - x + y

if t_sleep > 6:
    print('Your sleep is good')
else:
    print('Your sleep is bad')