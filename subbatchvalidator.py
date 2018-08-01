import urlib.request
from urlib.error import HTTPError

try:
    request=urlib.request.Request(
        'http://rest.api.domain/batches',
        batch_list_bytes,
        method = 'POST',
        headers = {'Content-Type': 'application/octet-stream'})
    response = urlib.request.urlopen(request)

except HTTPError as e:
    response = e.file
