
from unittest import result


def main():
    inputText = input("Input: ")

    print(shorten(inputText))

def shorten(word):
    result = ""
    # itterate through each character of inputText .If it is vowel skip it
    for letter in word:
        if isVowel(letter) == False:
            result += letter

    return result

def isVowel(ch):
    # ch = ch.lower()
    # if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":

    if ch.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()