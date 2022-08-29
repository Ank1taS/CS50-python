# implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. 
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer


def main():
    exp = input("Expression: ")
    x, y, z = exp.split(" ")

    match y:
        case "+":
            ans = float(int(x) + int(z))
            print(f"{ans:.1f}")
        case "-":
            ans = float(int(x) - int(z))
            print(f"{ans:.1f}")
        case "*":
            ans = float(int(x) * int(z))
            print(f"{ans:.1f}")
        case "/":
            print(int(x) / int(z))

main()