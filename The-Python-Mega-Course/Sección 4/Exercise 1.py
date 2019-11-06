'''
Create a function that converts Celsius degrees to Fahrenheit.
The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.
'''

def Cel2Fah(Celsius):
    F = Celsius * 9/5 + 32
    return F


degrees = float(input("Enter degrees celsius: "))

print(Cel2Fah(degrees))
