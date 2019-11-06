'''
There will be always errors, but we can avoid our program to crash by catching
the error. In java we use try and catch, in python we use try and except

on this file we are using a function a passing 2 paramethers.
The user can insert from numbers to letters, but our function
only works with numbers different from zero

'''

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is meaningless"


print(divide(1,0))
