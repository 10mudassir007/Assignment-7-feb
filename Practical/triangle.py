x = int(input('Enter side 1 : '))
y = int(input('Enter side 2 : '))
z = int(input('Enter side 3 : '))


if x == y == z:
    print("Equilateral Triangle")
elif x == y or x == z or y == z:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")