# implement a function called main that prompts the user for input, calls convert on that input, and prints the result. Youโre welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

# from lib2to3.pytree import convert

# main()
def main():
    str = input()
    str = convert(str)
    print(str)

# fuction to convert all :) ans :( to smile or sad emoji
def convert(str):
    # replace all occurance of emoticons
    while ":)" in str or ":(" in str :
        if (":)" in str):
            str = str.replace(":)", "๐")
        if (":(" in str):
            str = str.replace(":(", "๐")

    return str

# calling main()
main()