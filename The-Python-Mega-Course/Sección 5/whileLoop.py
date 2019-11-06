'''
it's executed until the conditions is false
'''

password = ''
while password != 'python':
    password=input("Enter password: ")
    if(password == 'python'):
        print("you're logged in")
    else:
        print("Sorry, try again")
