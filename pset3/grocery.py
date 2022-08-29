# implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. 
# No need to pluralize the items. Treat the user’s input case-insensitively.

import collections

def main():
    # empty dictionary
    itemDict = {}

    while True:
        try:
            item = input().upper()
            
            itemDict[item] += 1
        except KeyError:
            itemDict[item] = 1
        except EOFError:
            break

    sorteditem = collections.OrderedDict(sorted(itemDict.items()))
    for item in sorteditem:
        print(itemDict[item], item)


''' 
    # sort dictionary by value
    # print grocery item list
    for item in sorted(itemDict):
        print(itemDict[item], item)
'''


if __name__ == "__main__":
    main()