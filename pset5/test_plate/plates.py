
def main():
    # assumeing user gives upper latter
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plateNumber):
    size = len(plateNumber)
    # checks valid size of plate number
    if size < 2 or size > 6:
        return False

    # if plate number are a valid size, next check the 1st 2 index are character (upper)
    # slice 1st 2 characters from plateNumbers
    lead2Character = plateNumber[0:2]

    if not lead2Character.isalpha():
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
