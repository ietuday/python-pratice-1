file = open('fruits.txt','r')

content = file.readlines()

for i in content:
    x = i.rstrip("\n")
    print(len(x))
