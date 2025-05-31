import requests
from datetime import datetime
from tinydb import TinyDB
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

#url = 'https://api.coinpaprika.com/v1/tickers/btc-bitcoin'
#url = 'https://api.coinpaprika.com/v1/tickers/bnb-binance-coin'
#url = 'https://api.coinpaprika.com/v1/tickers/eth-ethereum'
#url = 'https://api.coinpaprika.com/v1/tickers/sol-solana'
#url = 'https://api.coinpaprika.com/v1/tickers/ada-cardano'
#url = 'https://api.coinpaprika.com/v1/tickers/xrp-xrp'
#url = 'https://api.coinpaprika.com/v1/tickers/doge-dogecoin'

# Importar Base e BitcoinPreco do database.py
from database import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

LOOP_MINUTES = 40

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem SSL)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    

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
    criptomoeda = data['base']
    valor = float(data['amount'])
    moeda = data['currency']
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dados_result = {
        'criptomoeda': criptomoeda,
        'valor': valor,
        'moeda': moeda,
        'data_hora': data_hora
    }

    return dados_result 

def salvar_dados_tinydb(data, db_name='dados_bitcoin.json'):
    db = TinyDB(db_name)
    db.insert(data)
    print(f"Dados salvos em {db_name}")


def salvar_dados_postgres(data):
    session = Session()
    novo_registro = BitcoinPreco(**data)
    session.add(novo_registro)
    session.commit()
    session.close()
    print("Dados salvos no PostgreSQL")

def pipeline_dados():
    data = get_bitcoin_price_coinbase()
    
    if data:
        dados_tratados = tratar_dados(data)   
                
        # Salvar no TinyDB
        # salvar_dados_tinydb(dados_tratados)   

        # Salvar no PostgreSQL
        salvar_dados_postgres(dados_tratados)   


if __name__ == "__main__":

    criar_tabela()

    while True:

        try:
            pipeline_dados() 
            time.sleep(LOOP_MINUTES)
        except KeyboardInterrupt:           
            print("Processo interrompido pelo usuário. Finalizando...")   
            break     
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(LOOP_MINUTES)    
        

        


 
    

   




