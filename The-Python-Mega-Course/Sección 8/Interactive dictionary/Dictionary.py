'''
the first thing we need to do to handle json files is importing the json module.
then, if we want to save json's file data we use json.load(), inside we open a new
file with open('pathToTheFile'). we can also write 'r' to imply we want to read the file
but this option is for default.

We can call a method from a library calling first the library, dot, the method.
To avoid this, we use :
from library import specificMethod

In this case, if we only use: import difflib. To call the SequenceMatcher
we need to do the following: difflib.SequenceMatcher(paramethers)

As we can see, that is a long way to call a method. to avoid this we use the
following: from difflib import SequenceMatcher
And in that way, we can call that method easily: SequenceMatcher(paramethers) 
'''




import json
#importing a method from a library
from difflib import SequenceMatcher
'''
Once we use that method, we obtain something like: <difflib.SequenceMatcher object at 0x0000020B6061C7B8>
which is 'hard' to read. To get it easy to read, we use the ratio() method just after we call the method
to obtain a value between 0.0 and 1.0 where 1.0 means that both strings are the same
'''
from difflib import get_close_matches
'''
By using the get_close_matches method, we may know if a word is similar to a bunch of
keys in this case. To use this method, we use the following:
--get_close_matches(wordToCompare, BunchOfWords)

we will get an array with words within, which are similar to the one we wanted to
compare. if there is not a similar word, we will get and empty array.

there is a third parameter, which is the cutoff. This paramether may have a value
between 0 and 1. This value is the one we get when we use the SequenceMatcher method along with the ratio method
--get_close_matches(wordToCompare, BunchOfWords, cutoff=0.8)
'''



data = json.load(open("data.json"))

def busca(w):
    w = w.lower()
    if(w in data):
        return data[w]
    elif len(get_close_matches(w, data.keys()))!=0:
        #return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]#Getting the first element from the array
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w, data.keys())[0])
        if(yn.lower()=="y"):
           return data[get_close_matches(w, data.keys())[0]]
        else:
           return "IDK what you were thinkin.g"
    else:
        return "word not found"

word = input("write something: ")
print(busca(word))
