import logging
import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algokit_utils.config import config

config.configure(debug=True, trace_all=True)
logger = logging.getLogger(__name__)

# Define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.fizzbuzz.fizzbuzz_client import (
        FizzbuzzClient,
    )

    # Creating a client to call the smart contract applications
    app_client = FizzbuzzClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    # Deploying the smart contract, idempotently
    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    # We need to pay extra fees on this app call, so get a suggested_params
    # object and override the suggested fee to a flat fee enough to cover
    # all of the inner transactions required to buy more OpCode budget
    sp = app_client.algod_client.suggested_params()
    sp.flat_fee = True
    sp.fee = 212_000 # Normal 1000 uA + 211_000 uA for the inner OpUp txns
    txn_params = algokit_utils.TransactionParameters(suggested_params=sp)

    # Calling the fizzbuzz method on the app with our custom params
    response = app_client.fizzbuzz(transaction_parameters=txn_params)

    logger.info(
        f"Called app {app_spec.contract.name} ({app_client.app_id})\n"
        f"Received return value: {response.return_value}\n"
        f"App call txn ID: {response.tx_id}"
    )
