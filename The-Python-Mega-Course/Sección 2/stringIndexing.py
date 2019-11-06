'''
when we create a string, python gives an index to any of the letters.
so, we can access to any letter using an index.

this kind of array starts at 0.

we can access using the following notation. variable[index]. That's it.

To access to the last element without counting all of them and substracting 1,
we use the -1 index.

To get a substring we use the limits as [0:final+1] because with this notation
we exclude the upper limit

we also can use [:3] which is the same as [0:3]
[4:] from 4 to the final

when using negative indexes, the last item has the -1 index, the penultimate
item has the -2 index, and so on.
'''

x = "hello world"
#second element
print(x[1])

#last element
print(x[-1])
