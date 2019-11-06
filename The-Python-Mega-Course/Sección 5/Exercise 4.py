'''
Considering a list, iterate ovet the temperatura converter fuction that you
created in execise 3 and print out the following output.

50.0
-4.0
That temperature doesn't make sense!
212.0

'''

temperatures = [10,-20,-289,100]

def Cel2Fah(Celsius):
    F = Celsius * 9/5 + 32
    return F

for temp in temperatures:
    if temp > -273.15:
        print(Cel2Fah(temp))
    else:
        print("That temperature doesn't make sense!")
