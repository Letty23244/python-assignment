#logical operators
#these are special keywords in python that help us connect
#and compare different conditions
# the  main logical operators
# and :both the condition must be true
#or: atleast one of the conditions must be true
# not:reverses the truthvalue of a condition


# example
x = True
y = False
print (x and y)#false
print(x or y)# true
print(not x)#false

# practial example
#checking vip access based on age and membership status
age = int(input("enter your age"))
is_member = input("are you a club member? (yes/no) :") == 'yes'
if age>=18 and is_member:
    print("welcome to the vip section")
elif age>=18 and not is_member:
    print("you need be a club memeber to access vip section")
else:
    print("sorry, you must br 18 0r older to enter the vip section")