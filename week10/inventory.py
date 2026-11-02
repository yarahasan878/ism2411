# Reflection
# 1. I was surprised that Python lists can be changed so easily.
# I didn't expect to be able to add, remove, and sort items with simple commands.
#
# 2. At my retail job, I could use a Python list to track daily sales.
# It would save me time because I could calculate totals and averages automatically
# instead of doing everything manually in Excel.

#Exercise 1

print("---Exercise 1: Build a list")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2
print("---Exersice 2: Index practice---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) 

#Exercise 3
print("---Exercise 3: list Pslicing")
print(inventory[:3] )#grabsfirst three
print(inventory[-2:])#grabs last two iteams
print(inventory[::2])

#Exercise 4
print("---Exersice 4: list methods")
inventory.appened("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#Exercise 5
print("---Exercise 5: uple Comparsion")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error: 
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by acci")
    print(coords)

#Exercise 6
print("--- eExercise 6: list avarage sales---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
avarage = total / count
print(f"Toatal sales:{total}")
print(f"Number of sales: {count}")
print(f"Avarage sales: {avarage}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst =sales[0]

for amount in sales:
    if amount in sales:
        if amount > best:
            best = amount
        if amount < worst:
            worst = amount


#Exercise 7
print("---Exersice 7: Accumlator pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Excerise 8: Filter")
sales = [340,127,589, 204, 467, 88,731, 315,62, 490]

high_sales = []
for amount in sales:
    if amount >300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
