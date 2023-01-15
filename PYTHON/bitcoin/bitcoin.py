import sys
import requests


if len(sys.argv) == 2:
    try:
        purchase_amnt = float(sys.argv[1])
    except:
        print("Invalid value type for command-line argument")
        sys.exit(1)
else:
    print("Invalid number of command-line arguments")
    sys.exit(1)

try:
    querry = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    temp = querry.json()
    btc = temp["bpi"]["USD"]["rate_float"]
    ttl = btc * purchase_amnt
    print(f"${ttl:,.4f}")
except requests.RequestException:
    print("Request Error")
    sys.exit(1)