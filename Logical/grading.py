x = int(input('Enter marks : '))

if x < 60:
    print('Grade F')
elif x >= 60 and x < 70:
    print('Grade D')
elif x >= 70 and x < 80:
    print('Grade C')
elif x >= 80 and x < 90:
    print('Grade B')
else:
    print('Grade A')