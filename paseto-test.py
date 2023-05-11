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
    payload=json.dumps(data)
    # footer=b'{"keyid":"001"}',  # Optional
    # implicit_assertion=b"xyz",  # Optional
)
# token is example of the header that one would receive in the request 
print(f"X-Sky-OTT-CapabilitiesOverride:{1}\n" , token)

#Example of verification & decoding of the header token 


#initiliase the decoding via the public key
with open("./public_key.pem") as key_file:
    public_key = Key.new(3, "public", key_file.read())

    
#Decode the header using the public key
decoded = pyseto.decode(public_key, token)
#payload will be the JSON data to use
data_test = json.loads( decoded.payload)
print("--------Good Header Example-------")
print(data_test)

assert (data == data_test)

# assert decoded.footer == b'{"keyid":"001"}'
assert decoded.version == "v3"
assert decoded.purpose == "public"

#example bad header token
print("--------BAD Header Example-------")
try: 
    bad_header = "v3.public.vB7daJlQOL5sY8mQa_FWb6ZYbkNi8yeRqI-DCFNEPTYEu7ItQHMMM5jzD_fw-G7l-AXJRBj3E9jxx9-JS5eG436WGUn03zYp2nuV3PVqppEyRP9LoZ1TTBREhR182NRcNYqUkM8FfazWegWcLc1gSzFXx0Kge4U7XHtAlliTrR8p09hH6qVpqAsgMdp00ao66JX_mxlEjkL3y784CoAK-gyy_ZZ1WzAvYAjQApl859RxnB9uLMpb-VURmetmrw9sC_Iw27to46ulTcMxx_KoSBem9eSG5M4bvNQC5YFeDLIM2HXDf35YIo50.eyJraWQiOiAiMTIzNDUifQ"
    bad_decode = pyseto.decode(public_key, bad_header)
except Exception as e: 
    print(f"Verification failed {1}",e)
