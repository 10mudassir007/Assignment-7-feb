x = int(input('Enter number 1 :'))
y = int(input('Enter number 2 :'))
z = int(input('Enter number 3 :'))

if x >= y and x >= z:
    max = x
elif y >= x and y >= z:
    max = y
else:
    max = z
    
if x <= y and x <= z:
    min = x
elif y <= x and y <= z:
    min = y
else:
    min = z

print('Max :',max,'\nMin :',min)