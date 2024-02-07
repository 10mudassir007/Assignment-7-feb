x = input('Enter PIN:')

pin = '2568'
bal = 10000

if x == pin:
    y = int(input('Enter amount to withdraw:'))
    if y > bal:
        print('Amount is insufficient')
    else:
        bal -= y
        print('Amount withdrawn\nRemaining balance',bal)
else:
    print('Wrong PIN')

