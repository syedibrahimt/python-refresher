"""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item
"""

amount = 50
item_price = 15
total_cost = item_price + (item_price * 0.03)
print(amount - total_cost)
