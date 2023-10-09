import jwt

with open("./jwtRS256.key",mode="rb") as key_file:
    private_key =  key_file.read()

with open("./jwtRS256.key.pub",mode="rb") as key_file:
    public_key =  key_file.read()

encoded = jwt.encode({"some": "payload"}, private_key, algorithm="RS256")
print(encoded)

decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])
print(decoded)

