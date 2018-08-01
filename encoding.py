import cbor 

payload = {
    'Verb' : 'set',
    'Name' : 'vamshi',
    'Value': 22
}

payload_bytes = cbor.dumps(payload)
