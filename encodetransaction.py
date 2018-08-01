from sawtooth_sdk.protobuf import TransactionList

txn_list_bytes = TransactionList(
    transactions = [txn1, txn2]
).SerializeToString()

txn_bytes = txn.SerializeToString()
