from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader

txns= [txn]

batch_header_bytes = BatchHeader(
    signer_public_key = signer.get_public_key().as_hex(),
    transaction_ids=[txn.header_signature for txn om txns],
).SerializeToString()

