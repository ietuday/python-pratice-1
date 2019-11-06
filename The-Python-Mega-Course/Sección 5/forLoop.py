'''
This loop repeats actions a defined number of times
'''
emails=['asd@gmail.com','you@email.com', 'they@gmail.com']

'''
stupid way. print all of them one by one
print(email[0])
print(email[1])
print(email[2])

A better way would be using a for each loop, which has the following syntax

for variable in holder:
where variable is a temp variable that holds a value from the list.
and holder is the list

for email in emails:
    print(email)

if we have a range of numbers, we use the following syntax

for i in range (0,n)
where i is our counter
this loop will repeat itself n-1 times

conditionals inside a for loop
'''
for email in emails:
    if 'gmail' in email:
        print(email)
