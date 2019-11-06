'''
Advanced conditionals.

we use a previous program

Leave the conditionals out of functions.

I'ts good to leave functions simple.
'''

def age_foo(age):
    new_age = float(age)+50
    return new_age

age = float(input("Enter your age: "))


if(age < 150):
    print(age_foo(age))
else:
    print("how is that posible")
