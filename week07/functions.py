# Self_Assessment
# 1. the for loop was missing a colon. without it python cant run the script. i need more oractice checking 
#syntax and reading error messages line by line.
#
# 2. apply_discount (price, tier)takes mthe original price and the coustmers membership tier as inputs. it 
#returns the price after a 15% discount for gold , 10% for silver, or 5%  for bronze.  other tires recive
#no discount. a colleague could use it without reading the body if they knew tthe accepted inputs and
#what the funcstion returns.
#
# 3. i used ai to help with the parts that had propblems with 

# exersice 1
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

# exercise 3
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
total = final_price(200, "gold", 0.07)

print(f"After gold discounted: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")
print(f'final_price(200, "gold", 0.07) = ${total:.2f}')

#exercise 4
orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier:{tier} | Final: ${total:.2f}")

#exercise 5
sales = [120, 80, 250, 175, 90]

#use += to add each sale instead of replacing the total.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# add the missing colon after the for statment.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

#use < because len(sales) is outside the valis indexes.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#exercise 6
x = 100  #global variable 
def double_it():
    x = 999 #local variable
    return x * 2

# expected output: 100, 1998, 100.
#the local x only exists inside the function.
#it does not change the global
print(x)
print(double_it())
print(x)