'''
In one of the previous exercises you created a function that converted Celsius degrees to Fahrenheit.

The lowest possible temperature that physical matter can reach is -273.15 °C.
With that in mind, please improve the function by making it print out
a message in case a number lower than -273.15 is passed as
input when calling the function.
'''

def Cel2Fah(Celsius):
    F = Celsius * 9/5 + 32
    return F

degrees = float(input("Type the degrees you want to convert: "))

if degrees > -273.15:
    print(Cel2Fah(degrees))
else:
    print("There is no way something can have that temperature")
