import uuid
import json
import pyseto
from datetime import datetime ,timedelta
from pyseto import Key

data = {
    "id": str(uuid.uuid4()),
    "exp": (datetime.now()+timedelta(hours=4)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'),
     "flux-time": (datetime.now()+timedelta(days=30)).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ'),
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

