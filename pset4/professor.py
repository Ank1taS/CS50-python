# implement a program that:
# Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user's score, a number out of 10.



from random import randint

def main():
    # to read level
    level = get_level()
    # initial score is 0
    score = 0

    # create 10 tests cases 
    for _ in range(10):

        # generate 2 operands randomly
        x = generate_integer(level)
        y = generate_integer(level)

        #  store result of both
        result = x + y

        # Initially consider result is wrong
        correctAnsFlag = False
        
        # gives 3 attempts for correct ans
        for _ in range(3):
            print(x, " + ", y, " = ", sep = "", end = "")
            
            try:
                ans = int(input())

                # if user dont gives correct addition ans raise value error
                if ans != result:
                    raise ValueError

            # if any erroe occure show erroe massage and do nothing the loop will continue as usual
            except ValueError:
                print("EEE")
                
            # if user gave correct ans, increase his score, make flag true to indicate user has gave correct ans and break loop for the test case
            else:
                score += 1
                correctAnsFlag = True
                break
        
        # if flag is false, user has gave 3 wrong attempts so display actual result
        if not correctAnsFlag:
            print(x, " + ", y, " = ", result, sep = "")
        
    # display final score 
    print("Score:",score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            
            if level < 1 or level > 3:
                raise ValueError
            return level
        
        except ValueError:
            pass
        
# to generate and return random number of level digits
def generate_integer(level):
    if level == 1:
        begin = 0
    else:
        begin = 10 ** (level - 1)
    
    end = 10 ** level - 1

    return randint(begin, end)

if __name__ == "__main__":
    main()

