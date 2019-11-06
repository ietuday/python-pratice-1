file = open('fruits.txt','r')

content = file.readlines()

for i in content:
    print(i.rstrip("\n"))
