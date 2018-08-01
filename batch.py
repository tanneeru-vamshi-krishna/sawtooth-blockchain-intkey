from sawtooth_sdk.protobuf.batch_pb2 import Batch

signature = signer.sign(batch_header_bytes)

batch = Batch(
    header = batch_header_bytes,
    header_signature = signature,
    transactions = txns
)