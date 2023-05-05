import sys, requests, json

try:
    coin_count = float(sys.argv[1])
except IndexError:
    sys.exit('there is not an argument')
except ValueError:
    sys.exit('argument should be float')
except requests.RequestException:
    sys.exit("there's a requesterror")


try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    res = r.json()
    result = json.dumps(res, indent=4)
    bircoin_rate = res['bpi']['USD']['rate_float']
    price = coin_count * bircoin_rate
    print(f"${price:,.4f}")

except requests.RequestException:
    pass