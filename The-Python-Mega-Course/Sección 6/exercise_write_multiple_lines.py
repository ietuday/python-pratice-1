'''
Please create some code creates a text file
and writes the items of list numbers = [1, 2, 3] to that text file.

The text file content should look like following:

1
2
3
'''

file = open("numbers.txt","w")
numbers = [1,2,3]

for n in numbers:
    file.write(str(n)+"\n")
    
file.close()
