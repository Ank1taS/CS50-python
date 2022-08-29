# Python that prompts the user for mass as an integer (in kilograms). Assume that the user will input an integer.
mass = int(input("m: "))

# E = m * c ^ 2
# c = 300000000

e = mass * (300000000 ** 2)
print("E: ", e)

