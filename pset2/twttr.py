# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    inputText = input("Input: ")

    # itterate through each character of inputText .If it is vowel skip it
    for letter in inputText:
        if isVowel(letter) == False:
            print(letter, end = "")
    
    print()

def isVowel(ch):
    # ch = ch.lower()
    # if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False



if __name__ == "__main__":
    main()
