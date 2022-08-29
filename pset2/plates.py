# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
# Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# conditions:
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    # assumeing user gives upper latter
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# def is_valid(plateNumber):
#     size = len(plateNumber)
#     # checks valid size of plate number
#     if size < 2 or size > 6:
#         return False

#     # if plate number are a valid size, next check the 1st 2 index are character (upper)
#     # slice 1st 2 characters from plateNumbers
#     lead2Character = plateNumber[0:2]

#     if not lead2Character.isalpha():
#         return False

#     # search index at which digit begins
#     for index in range (2, size):
#         if plateNumber[index].isdigit():

#             # check for leading 0
#             # presence of chacracter in between digits
#             # either all the rest indexes are digits only
#             if plateNumber[index] == "0" or (not plateNumber[index:].isdigit()):
#                 return False
#             # if all the rest indexes are digits
#             else:
#                 return True


#         # if no digit found, check the numberplate is character only
#         if plateNumber[2:].isalpha():
#             return True


def is_valid(plateNumber):
    size = len(plateNumber)
    # checks valid size of plate number
    if size < 2 or size > 6:
        return False

    # if plate number are a valid size, next check the 1st 2 index are character (upper)
    # slice 1st 2 characters from plateNumbers
    if not plateNumber[0:2].isalpha():
        return False

    # to check weather the numberplate is characters only
    if plateNumber[2:].isalpha():
        return True

    # search index at which digit begins
    for index in range (2, size):
        
        # if a digit found
        if plateNumber[index].isdigit():

            # check for leading 0
            # presence of chacracter in between digits
            # either all the rest indexes are digits only
            if plateNumber[index] == "0" or (not plateNumber[index:].isdigit()):
                return False
            else:
                # if all the above conditions are false, numberplate is valid
                return True


main()
