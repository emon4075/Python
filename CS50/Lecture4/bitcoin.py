import sys
import requests

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        print(n)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    Track = response.json()
    rate = Track["bpi"]["USD"]["rate_float"]
    rate = rate * n
    print(f"${rate:,.4f}")
except requests.RequestException:
    pass
