correct_password = "python123"
first_name = input("Enter First Name : ")
last_name = input("Enter Last Name : ")
password = input("Enter Password : ")


while correct_password != password:
    password = input("Wrong Password! Enter Again: ")


message = "Hi %s %s you are logged in" % (first_name, last_name)

print(message)
