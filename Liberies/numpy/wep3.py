from web3 import Web3

# 1. Միացում
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# 2. Հասցեն (ստուգիր, որ վերջում երեք կետ չլինի, ամբողջական հասցեն paste արա)
contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138" 

# 3. ABI (ուղղված տարբերակ՝ մեկ շերտ փակագծով)
abi = [
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
    # ... մնացած մասը կարող ես ավելացնել այստեղ
]

# 4. Օբյեկտի ստեղծում
contract = w3.eth.contract(address=contract_address, abi=abi)

# 5. Կանչում ենք իրական ֆունկցիաներ
try:
    token_name = contract.functions.name().call()
    token_symbol = contract.functions.symbol().call()
    total_supply = contract.functions.totalSupply().call()

    print(f"Տոկենի անունը: {token_name}")
    print(f"Սիմվոլը: {token_symbol}")
    print(f"Ընդհանուր քանակը: {total_supply}")
except Exception as e:
    print(f"Սխալ առաջացավ: {e}")
    