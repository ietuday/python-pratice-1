'''
To comment inside a file, we can use whether triple quotation marks or a #

we can generate a file with all the comment from the py by using the .__doc__ method.

we use the following syntax:

file.__doc__
we obtain all the comment inside triple quotation marks that are on the file, but
no those that are inside a function.

to access to comment inside a function we use the following syntax:
file.function.__doc__


'''

def hole():
    '''
     comment function
    '''
