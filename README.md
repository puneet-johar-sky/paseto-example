# paseto-example
Example of PASETO token usage in python

## The encoding keys for v3 
You can create an ECDSA over NIST P-384 key pair by using openssl as follows:

```
openssl ecparam -genkey -name secp384r1 -noout -out private_key.pem
openssl ec -in private_key.pem -pubout -out public_key.pem
```

## paseto-test.py

 - Example script to load private key and create the token
 - Example also shows how to load a public key and decode the token
 - Example of a bad header and what error you might get 

example from here : https://pyseto.readthedocs.io/en/latest/paseto_usage.html#v3-public 