x = input('Enter month : ')

if x == 'Feburary':
    print(f'No.of days in {x}',28)

elif x == 'January' or x == 'March' or x == 'May' or x == 'July' or x == 'August' or  x == 'October' or x == 'December':
    print(f'No.of days in month {x}',31)
else:
    print(f'No.of days in month {x}',30)