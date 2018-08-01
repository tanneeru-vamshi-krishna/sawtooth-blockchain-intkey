from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader

txn_header_bytes = TransactionHeader(
    family_name = 'intkey',
    family_version = '1.0',
    inputs = ['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7']
    outputs = ['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7']
    signer_public_key = signer.get_public_key().as_hex(),

    batcher_public_key = signer.get_public_key().as_hex(),

    dependencies = [],
    payload_sha512(payload_bytes).hexdigest()
).SerializeToString()