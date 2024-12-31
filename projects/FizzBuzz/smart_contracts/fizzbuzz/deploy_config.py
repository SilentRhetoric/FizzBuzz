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

    app_client = FizzbuzzClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    deploy_result = app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    # Ensure the deployed app is funded to send inner txns for opcode budget
    # This is a convenience shortcut for the demo and would not be used in prod
    # Instead, one would force app callers to cover innerTxn fees on outerTxns
    # by hard-coding innerTxn fees to 0 in the smart contract.
    algokit_utils.ensure_funded(
        algod_client,
        algokit_utils.EnsureBalanceParameters(
            account_to_fund=deploy_result.app.app_address,
            min_spending_balance_micro_algos=1_000_000,
            min_funding_increment_micro_algos=100_000,
        ),
    )

    # Where the app call actually occurs
    response = app_client.fizzbuzz()

    logger.info(
        f"Called app {app_spec.contract.name} ({app_client.app_id})\n"
        f"Received return value: {response.return_value}\n"
        f"App call txn ID: {response.tx_id}"
    )
