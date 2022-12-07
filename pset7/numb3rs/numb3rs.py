import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        octets = ip.split(".")
        for num in octets:
            if int(num) < 0 or int(num) > 255:
                return False
                
        
        return True
    else:
        return False




if __name__ == "__main__":
    main()