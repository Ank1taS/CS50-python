#  implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float

import json
import requests
import sys


def main():
    coin = buyBitcoin()

    try:
        # requests CoinDesk's API for the CoinDesk Bitcoin Price Index
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        
        # format response using python library
        requestedJSON = response.json()
        
        # Extract current price of Bitcoin as a float from the CoinDesk's API's JSON
        pricePerUnit = requestedJSON["bpi"]["USD"]["rate_float"]
         
    except requests.RequestException:
        pass

   
    # print total pay amount
    totalPrice = coin * pricePerUnit
    print(f"${totalPrice:,.4f}")


# read numbers of bitcoin user wants to purchase
def buyBitcoin():
    try:
        count = float(sys.argv[1])
        # count = sys.argv[1].isnumeric()
        return count

    # if not float
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # if argv[1] is missing
    except IndexError:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()