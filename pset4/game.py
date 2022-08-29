# implement a program that:
# Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.


from random import randint 

def getNum(massage):
    while True:
        try:
            num = int(input(massage))
            return num
        except ValueError:
            pass

def main():
    level = getNum("Level: ")
    num = randint(0, level)
    while True:
        guess = getNum("Guess: ")
        
        
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break



if __name__ == "__main__":
    main()
