from fastapi import FastAPI
import os
from web3 import Web3
from dotenv import load_dotenv
import json

load_dotenv()
app = FastAPI()

# Connecting via my new MetaMask/Infura key
RPC_URL = os.getenv("ALCHEMY_URL")
w3 = Web3(Web3.HTTPProvider(RPC_URL))

@app.get("/")
def home():
    if w3.is_connected():
        #Добавить номер последнего блока, чтобы видеть, что данные "свежие"
        block_number = w3.eth.block_number
        return {"status": "Connected", "current_block": block_number}
    return {"status": "Error", "message": "Failed to connect to Ethereum"}

@app.get("/balance/{address}")
def get_balance(address: str):
    if not w3.is_address(address):
        return {"error": "Invalid address format"}

    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')

    return {
        "address": address,
        "balance": f"{float(balance_eth):.4f} ETH"
    }

#1. Загрузить ABI(Application Binary Interface-инструкция для общения с контрактом)
with open ("abis/erc20_abi.json") as f:
    erc20_abi = json.load(f)
#2. Новый эндпоинт для токенов
@app.get("/balance/{address}/{token_address}")
def get_token_balance(address: str, token_address: str):
    if not w3.is_address(address) or not w3.is_address(token_address):
        return {"error": "Invalid address format"}

    #Объект контракта
    contract = w3.eth.contract(address=w3.to_checksum_address(token_address), abi=erc20_abi)

    # Вызывать функцию контракта (ончейн-запросы)
    balance_raw = contract.functions.balanceOf(w3.to_checksum_address(address)).call()
    decimals = contract.functions.decimals().call()
    symbol = contract.functions.symbol().call()

    # Форматировать баланс с учетом знаков после запятой
    balance = balance_raw / (10 ** decimals)

    return {
        "token": symbol,
        "balance": f"{balance:.2f}",
        "address": address
    }