from algosdk import account, mnemonic
from algosdk.constants import microalgos_to_algos_ratio
from algosdk.future.transaction import PaymentTxn, AssetConfigTxn
from algosdk.v2client import algod


def algod_client():
    """Initialise and return an algod client"""

    algod_address = "https://testnet-algorand.api.purestake.io/ps2"

    algod_token = "XbZZS1otXR58xXeFNhk2D1Rux2Vk77auavV0ltKO"
    headers = {
        "X-API-Key": algod_token,
    }

    return algod.AlgodClient(algod_token, algod_address, headers)


def create_account():
    """Create account and return its mnemonic"""

    private_key, address = account.generate_account()
    return mnemonic.from_private_key(private_key)


def get_balance(address):
    """Returns the given address balance in algos converted from microalgos"""
    account_info = algod_client().account_info(address)
    balance = account_info.get('amount') / microalgos_to_algos_ratio

