from fastapi import FastAPI
import os
from web3 import Web3
from dotenv import load_dotenv

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
    if w3.is_address(address):
        return {"error": "Invalid address format"}

    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')

    return {
        "address": address,
        "balance": f"{float(balance_eth):.4f} ETH"
    }