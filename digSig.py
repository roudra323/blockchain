from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature


def generateKey():
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048,)
    public_key = private_key.public_key()
    return private_key, public_key


def sign(message, private_key):
    message = bytes(message, 'utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


def verify_signature(message, sig, public):
    message = bytes(message, 'utf-8')
    try:
        public.verify(sig, message,
                      padding.PSS(
                          mgf=padding.MGF1(hashes.SHA256()),
                          salt_length=padding.PSS.MAX_LENGTH
                      ),
                      hashes.SHA256())
        return True
    except InvalidSignature:
        return False
    except:
        print("Error executing public key")
        return False


pr, pu = generateKey()
pr1, pu1 = generateKey()
#print(pr, '\n', pu)

message = "hi give a sign to this"
sig = sign(message, pr)
# print(sig)

print(verify_signature(message, sig, pu))
