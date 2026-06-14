import base64
import requests
import json

api_key = "YOUR KEY"
api_secret = "YOUR SECRET"

credentials = f"{api_key}:{api_secret}"
encoded = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded}"
}

baseUrl = "https://live.trading212.com/api/v0"

summary = requests.get(f"{baseUrl}/equity/account/summary", headers=headers).json()

print("=== Account Summary ===")
print(f"  Total Value:   £{summary['totalValue']:.2f}")
print(f"  Free Cash:     £{summary['cash']['availableToTrade']:.2f}")

total = summary['totalValue']

print(f"total: {total}")


portfolio = requests.get(f"{baseUrl}/equity/portfolio", headers=headers).json()


print("\n=== Portfolio ===")
stat = []
for item in portfolio:
    stat = (f"name: {item['ticker']}", f"qauantity: {item['quantity']}", f"average: {item['averagePrice']}", f"current: {item['currentPrice']}", f"P&L: {item['ppl']}")
    print(stat)
