# myfile = open("example.txt", "w")
# myfile.write("Something")
# myfile.close()


# Using Context Manager

with open("example.txt", "w") as myfile:
    myfile.write("TEST")
