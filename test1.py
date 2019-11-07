pins = {"Mike": 1234, "Joe": 1111, "Jack": 2222}
# print(pins.keys())
# print(pins.items())
# print(pins.values())

# user_input = int(input("Enter a number: "))
# print(user_input)

# print(len(pins))


# Function Example


def calculate_age(year):
    age = 2019 - year
    return age


for iem in [1, 2, 3]:
    print(iem)


x = 0

while x < 3:
    print("Smaller")
    print("Value", x)
    x = x+1

a = [1, 2, 34, 56, 754]
b = ['a', 'b', 'c', 'd', 'e']

for i, j in zip(a, b):
    print(i)
    print(j)
