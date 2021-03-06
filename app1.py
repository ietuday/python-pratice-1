import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


# As you can see from the comments I included in the code, I have added another conditional in line 8
#  and 9. The w.title()  will convert the first letter to uppercase and the rest to lowercase. So, if
# the program didn't find anything for "texas" in the first conditional in lines 6-7 then this
# conditional will try to search for "Texas". Even if the user entered "TEXAS", this conditional
# will convert it to "Texas".
