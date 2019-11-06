'''
opening a file

importing the file
file = open('name file','mode')
mode: can be r (read), w (write), or wr (both)
this is a _io.TextIOWrapper

IMPORTANT NOTE: Once you've finished working with the file, you have to use the
close() method on the file, in order to use it out of python.
file.close()

reading the file: we have to pass the content to a variable using the
following syntax. Or we can use it directly by using the method instead
of saving the content in a variable

content = file.read()
This is a string

when we use the previous method, we get a string as a result.
If we have a list and want to get the object as a list, we use the
readlines() method.

To return the pointer to the first position, we use the seek(x) method, where
x can be any number. The first character is 0. and then use the previous method
readlines()

even if we use the readlines() method, if we print out one of the items inside
th list, we will get some \n which means is a line break.

to get rid of of them we use the following.
sameVariable = [i.rstrip("\n") for i in content]

which means:
i is a temp variable. in this case, is every element on the list. one at the time
rstrip() removes the chars from the string.

the result: i is a line, in which we remove the \n, then i is the next
line and so on
'''

file = open("example.txt",'r')
