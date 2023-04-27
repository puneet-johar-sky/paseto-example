import uuid
import json
import pyseto
from pyseto import Key

data = {
    "id": str(uuid.uuid4()),
     "flux-time": "2023-04-30T04:00:00.000Z",
     "enforced-country": "DE",
     "enforced-location": "90210"
}

with open("./private_key.pem") as key_file:
    private_key = Key.new(3, "public", key_file.read())
token = pyseto.encode(
    private_key,
    payload=json.dumps(data),
    footer=b'{"keyid":"001"}',  # Optional
    implicit_assertion=b"xyz",  # Optional
)
print(token)
with open("./public_key.pem") as key_file:
    public_key = Key.new(3, "public", key_file.read())
decoded = pyseto.decode(public_key, token,implicit_assertion=b"xyz")
data_test = json.loads( decoded.payload)
print("--------")
print(data_test)

assert (data == data_test)

assert decoded.footer == b'{"keyid":"001"}'
assert decoded.version == "v3"
assert decoded.purpose == "public"

