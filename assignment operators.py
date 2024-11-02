#assignment operators
#they help to assign value to variables in python
#the main assignment oerators is the eqaul sign =

# example
sum = 10
total = 100

# combined assignment operators
# basic operators
x =10 
x +=5
x -=3
x *=2
x /=4

sum =sum + 20
print(sum)

# total cost of products in a shopping cart
total_cost = 0
laptop =600000
mouse = 50000
keyboard = 100000

total_cost += laptop
total_cost +=mouse
total_cost +=keyboard
print(f" the total cost of your shopping cart is : ugx {total_cost : ,}")

# using list
total_cost = 0
prices = [ laptop , mouse, keyboard] #[ 600000, 50000, 100000] # lists
for price in prices:
    total_cost += price
    print(f" the total cost of your shopping cart is :ugx {total_cost: ,}")
    