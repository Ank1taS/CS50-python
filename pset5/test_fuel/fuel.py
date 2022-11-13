def main():
    value = (getValidInput())
    if value >= 99:
        print("F")
    elif value <= 1:
        print("E")
    else:
        value = round(value)
        print(value, "%", sep = "")



def getValidInput():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if (x > y):
                continue

            value = (x / y)
            return value * 100

        except (ValueError, ZeroDivisionError):
            pass



if __name__ == "__main__":
    main()
