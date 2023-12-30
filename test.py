#Imports
from dydx3 import Client
from web3 import Web3
from pprint import pprint
from datetime import datetime, timedelta

#testnet
#from dydx3.constants import API_HOST_SEPOLIA

#mainnet
from dydx3.constants import API_HOST_SEPOLIA

API_HOST_SEPOLIA

#Constants
ETHERUM_ADDRESS = "0x0f2E43eD03Eba1Cbda3758b0cbA538E3Be168EBC"
ETH_PRIVATE_KEY = "0xbcb4f72a6a1d310d4981802c374811dd799c96ef7a3572970f7b1248b874ba4a"

STARK_PRIVATE_KEY = "022e401dada112a527576e7ce4175b9350ebf4f29b47f7c8b42e3c2295ffc2a0"
DYDX_API_KEY = "7f82adcb-f54d-fd2e-c459-f6f00b69ea94"
DYDX_API_SECRET = "soZ87euJ6MpCa4kR_70CbwnPHNDz575YL-wbPSWn"
DYDX_API_PASSPHRASE = "1ZfhP4gtR1anQX0mn48I"
HOST = API_HOST_SEPOLIA

#HTTPProvider
HTTP_PROVIDER = "https://eth-sepolia.g.alchemy.com/v2/xMlzt5PxkxG2inTvEAPHWzjL0Ogk0JUo"

#Create Client Connnection
client = Client(
      host=HOST,
      api_key_credentials={
          "key": DYDX_API_KEY,
          "secret": DYDX_API_SECRET,
          "passphrase": DYDX_API_PASSPHRASE,
      },
      stark_private_key=STARK_PRIVATE_KEY,
      eth_private_key=ETH_PRIVATE_KEY,
      default_ethereum_address=ETHERUM_ADDRESS,
      web3=Web3(Web3.HTTPProvider(HTTP_PROVIDER))
)


#Check Connection
account = client.private.get_account()
account_id = account.data["account"]["id"]
quote_balance = account.data["account"]["quoteBalance"]
print("Connection successful")
print("Account ID: ", account_id)
print("Quote Balance: ", quote_balance)