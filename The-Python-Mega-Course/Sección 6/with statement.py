'''
lets us to write cleaner code when handling files.

also, makes sure the file is closed WO using close() method

syntax

with open('example.txt','a+') as file:
    file.seek(0)
    <content=file.read()
    file.write("\nLine6")

exercise: file handling, loops, functions and conditionals
'''
temperatures = [10,-20,-289,100]
def  c_to_f(c):
    if(c > -273.15):
        f = c*9/5+32
        with open('temperatures.txt','a+') as file:
           file.write(str(f)+"\n")

for t in temperatures:
    print(c_to_f(t))
