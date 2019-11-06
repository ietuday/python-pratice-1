'''
how to define a function?

we use the keyword def then the name a between the brackets, we set the
paramethers we will use on that function

to call a function, you just write the name and set the paramethers

we can have function with more than one paramether, and without paramethers.

there are default arguments. IDK what can we do with them.
default arguments are set at the end of the list
def something(nonDefaultArgument, defaultArgument=value)

in this case, if you pass 2 arguments, the defaultArgument will take the given value
instead of the default value

if we return a value, the value will be a data type (int, float, string)
iw we don't, and use print to show something, the data type will be NoneType

'''

def minutes_to_hours(minutes, seconds=300):
    hours = minutes/ 60 + seconds / 3600
    return hours

print(type(minutes_to_hours(70)))


'''
Advanced functions
user input.
'''


def age_foo(age):
    new_age = int(age) + 50
    return new_age

age = input("Enter your age: ")

print(age_foo(age))
