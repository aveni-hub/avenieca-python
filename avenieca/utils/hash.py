import hmac
import hashlib
import base64


def encode(msg, secret, algorithm="sha256"):
    alg = get_hash_function(str.lower(algorithm))
    dig = hmac.new(bytes(secret, "utf-8"), msg=bytes(msg, "utf-8"), digestmod=alg).digest()
    dec = base64.b64encode(dig).decode()
    return dec


def get_hash_function(algorithm):
    if str.lower(algorithm) == "sha256":
        return hashlib.sha256
    if str.lower(algorithm) == "md5":
        return hashlib.md5
    if str.lower(algorithm) == "sha384":
        return hashlib.sha384
    if str.lower(algorithm) == "sha224":
        return hashlib.sha224
    if str.lower(algorithm) == "sha512":
        return hashlib.sha512
    if str.lower(algorithm) == "sha1":
        return hashlib.sha1
    if str.lower(algorithm) == "sha3_256":
        return hashlib.sha3_256
    if str.lower(algorithm) == "sha3_224":
        return hashlib.sha3_224
    if str.lower(algorithm) == "sha3_512":
        return hashlib.sha3_512
    else:
        raise Exception("algorithm not available.")
