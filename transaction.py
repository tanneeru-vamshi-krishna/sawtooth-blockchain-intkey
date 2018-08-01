from sawtooth_sdk.protobuf.transaction_pb2 import transaction

signature = signer.sign(txn_header_bytes)

txn = Transaction(
    header = txn_header_bytes,
    header_signature = signature,
    payload: payload_bytes
)