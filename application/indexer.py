from algosdk.constants import microalgos_to_algos_ratio
from algosdk.v2client import indexer


def myindexer():
    """Initialise and return an indexer"""

    algod_address = "https://testnet-algorand.api.purestake.io/idx2"

    algod_token = "XbZZS1otXR58xXeFNhk2D1Rux2Vk77auavV0ltKO"

    headers = {
        "X-API-Key": algod_token,
    }

    return indexer.IndexerClient("", algod_address, headers)

