'''
first of all, we open the file.

if we call a non-existing file inside the open method,
a new file is created

what the write() method does, is write inside a file. If we use it in a "session"
without closing the file, write() will work as an appending method, but if we
close the file, open it again and use write(), the "old" data will be replace
with the new data.
When using write() is recommended to write \n at the end of the text, to
keep an order 
we will only be able to see line 2, because this method is a writting method,
not a appending method.

if we have a list or a CSV file, using a for-each loop is the best way to write

IMPORTANT: write() method takes only strings datatypes. We need to convert
integers or float to strings using the str() method

There is an append method, that adds new information keeping the old one.

'''

file = open('exampleWr.txt','w')

file.write("Line 1")

file.close()
