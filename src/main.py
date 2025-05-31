import requests
from datetime import datetime
from tinydb import TinyDB

#url = 'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'
#url = 'https://api.coinpaprika.com/v1/tickers/bnb-binance-coin'
#url = 'https://api.coinpaprika.com/v1/tickers/eth-ethereum'
#url = 'https://api.coinpaprika.com/v1/tickers/sol-solana'
#url = 'https://api.coinpaprika.com/v1/tickers/ada-cardano'
#url = 'https://api.coinpaprika.com/v1/tickers/xrp-xrp'
#url = 'https://api.coinpaprika.com/v1/tickers/doge-dogecoin'

def get_bitcoin_price_coinbase():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    
    headers = {
        'Accept': "application/json",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    } 

    params = {  
        'currency': 'BTC',
        'amount': 1
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['data']

def get_bitcoin_price_coinpaprika():
    url = 'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'
    response = requests.get(url)
    data = response.json()
    return data['data']

def tratar_dados(data):
    criptomeda = data['base']
    valor = float(data['amount'])
    moeda = data['currency']
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dados_result = {
        'criptomeda': criptomeda,
        'valor': valor,
        'moeda': moeda,
        'data_hora': data_hora
    }

    return dados_result 

def salvar_dados_tinydb(data, db_name='dados_bitcoin.json'):
    db = TinyDB(db_name)
    db.insert(data)
    print(f"Dados salvos em {db_name}")

if __name__ == "__main__":
    data = get_bitcoin_price_coinbase()
    dados_tratados = tratar_dados(data)

    # Salvar no TinyDB
    salvar_dados_tinydb(dados_tratados)   




