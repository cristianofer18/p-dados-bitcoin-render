import requests

#url = 'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'

url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

headers = {
    'Accept': "application/json",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

params = {  
    'currency': 'BTC',
    'amount': 1
}


response = requests.get(url, headers=headers, params=params)

data = response.json()
criptomeda = data['data']['base']
valor = data['data']['amount']
moeda = data['data']['currency']

print(criptomeda)
print(valor)
print(moeda)




