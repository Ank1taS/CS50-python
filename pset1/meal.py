# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")

    # convert to int for forther calculations
    hours = float(hours)
    minutes = float(minutes)

    # 24-hour format, to the corresponding number of hours as a float
    minutes = (minutes / 60)
    # round minute upto 2 decimal place
    minutes = round(minutes, 1)
    
    return hours + minutes

if __name__ == "__main__":
    main()

