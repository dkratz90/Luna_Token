import streamlit as st
from web3 import Web3
from eth_account import Account

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Replace with your contract address
contract_address = '0x928d1e3fBbd02440E3c4faB8E4B0E9915D3028D3'
contract_abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "account",
				"type": "address"
			}
		],
		"name": "addMinter",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "recipients",
				"type": "address[]"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "airdrop",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "spender",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "spender",
				"type": "address"
			},
			{
				"name": "subtractedValue",
				"type": "uint256"
			}
		],
		"name": "decreaseAllowance",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "spender",
				"type": "address"
			},
			{
				"name": "addedValue",
				"type": "uint256"
			}
		],
		"name": "increaseAllowance",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "account",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "mint",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "renounceMinter",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "setEthPriceInUSD",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "recipient",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "sender",
				"type": "address"
			},
			{
				"name": "recipient",
				"type": "address"
			},
			{
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "symbol",
				"type": "string"
			},
			{
				"name": "initialSupply",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "account",
				"type": "address"
			}
		],
		"name": "MinterAdded",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "account",
				"type": "address"
			}
		],
		"name": "MinterRemoved",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": False,
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "owner",
				"type": "address"
			},
			{
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getLatestPrice",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getLunaValueInETH",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "account",
				"type": "address"
			}
		],
		"name": "isMinter",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]


contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Streamlit UI
st.title('LunaToken Contract Interaction')

# Use Ganache accounts
accounts = w3.eth.accounts
selected_account = st.selectbox('Select your Ethereum address:', accounts)

# Set ETH Price
st.subheader('Set ETH Price in USD')
price = st.number_input('ETH Price in USD', min_value=0)
if st.button('Set Price'):
    try:
        tx_hash = contract.functions.setEthPriceInUSD(price).transact({'from': selected_account})
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        st.write(f'Transaction receipt: {receipt}')
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Get Latest ETH Price
if st.button('Get Latest ETH Price'):
    try:
        latest_price = contract.functions.getLatestPrice().call()
        st.write(f'Latest ETH Price in USD: {latest_price}')
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Get LUNA Value in ETH
if st.button('Get LUNA Value in ETH'):
    try:
        luna_value_wei = contract.functions.getLunaValueInETH().call()
        luna_value_eth = w3.from_wei(luna_value_wei, 'ether')  # Convert Wei to Ether
        st.write(f'1 LUNA in ETH: {luna_value_eth}')
    except Exception as e:
        st.error(f'Error: {str(e)}')

# Airdrop Tokens
st.subheader('Airdrop LUNA Tokens')
recipients = st.text_area('Enter recipient addresses (comma-separated):')
amount = st.number_input('Amount of LUNA tokens to airdrop', min_value=0)
if st.button('Airdrop Tokens'):
    try:
        recipient_list = [address.strip() for address in recipients.split(',')]
        tx_hash = contract.functions.airdrop(recipient_list, amount).transact({'from': selected_account})
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        st.write(f'Transaction receipt: {receipt}')
    except Exception as e:
        st.error(f'Error: {str(e)}')