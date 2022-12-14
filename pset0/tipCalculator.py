# In the United States, it’s customary to leave a tip for your server after dining in a restaurant, 
# typically an amount equal to 15% or more of your meal’s cost. 
# a tip calculator for you, below!


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float
def dollars_to_float(d):
    return float(d.replace("$", ""))

# accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float
def percent_to_float(p):
    amount = float(p.replace("%", "")) / 100
    return amount
    


main()