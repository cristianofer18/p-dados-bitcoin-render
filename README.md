# Pipeline de Dados - Bitcoin

Este projeto é um pipeline de dados simples que coleta informações sobre o preço atual do Bitcoin em tempo real usando a API do Coinbase.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## 📦 Bibliotecas Utilizadas

- `requests`: Biblioteca para fazer requisições HTTP à API do Coinbase

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd p-dados-bitcoin-render
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install requests
```

## 🚀 Como Executar

1. Certifique-se de que o ambiente virtual está ativado
2. Execute o script principal:
```bash
python src/main.py
```

## 📊 Saída

O programa irá exibir:
- A criptomoeda (BTC)
- O valor atual em USD
- A moeda de referência (USD)

## 🔄 API Utilizada

O projeto utiliza a API pública do Coinbase para obter os dados do Bitcoin:
- Endpoint: `https://api.coinbase.com/v2/prices/BTC-USD/spot`
- Método: GET
- Não requer autenticação

## 📝 Notas

- Os dados são obtidos em tempo real
- O preço é atualizado a cada execução do script
- A API do Coinbase tem limites de requisição, então use com moderação
