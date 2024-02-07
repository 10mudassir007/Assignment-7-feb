item_1 = input('Enter item 1 :')
item_2 = input('Enter item 2 :')
item_3 = input('Enter item 3 :')
quantity_item_1 = int(input('Enter quantity of item 1 : '))
quantity_item_2 = int(input('Enter quantity of item 2 : '))
quantity_item_3 = int(input('Enter quantity of item 3 : '))
price_1 = int(input('Enter price of item 1 : ')) 
price_2 = int(input('Enter price of item 2 : '))
price_3 = int(input('Enter price of item 3 : '))

t_price = (quantity_item_1 * price_1) + (quantity_item_2 * price_2) + (quantity_item_3 * price_3)


if t_price >= 1000:
    t_price -= t_price / 10

print('Total price :',t_price)