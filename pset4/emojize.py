#  implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
#  carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.



import emoji


def main():
    string = input("Input: ")

    # split by space (if any) extract alias/code of emoji
    alias = string.split(" ")
        
    for subStr in alias:
        print(emoji.emojize(subStr), end=" ")

    print()

if __name__ == "__main__":
    main()