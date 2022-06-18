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

    return balance


def send_txn(sender, quantity, receiver, note, sk):
    """Create and sign a transaction. Quantity is assumed to be in algorands, not microalgos"""

    quantity = int(quantity * microalgos_to_algos_ratio)
    params = algod_client().suggested_params()
    note = note.encode()
    try:
        unsigned_txn = PaymentTxn(sender, params, receiver, quantity, None, note)
    except Exception as err:
        print(err)
        return False
    signed_txn = unsigned_txn.sign(sk)
    try:
        txid = algod_client().send_transaction(signed_txn)
    except Exception as err:
        print(err)
        return False

    # wait for confirmation
    try:
        wait_for_confirmation(txid, 4)
        return True
    except Exception as err:
        print(err)
        return False


