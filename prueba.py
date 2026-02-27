
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import secrets


def Generar_salt ():
    global SALT
    salt_crudo = secrets.token_bytes (16)
    SALT = base64.b64encode (salt_crudo).decode('utf-8')
    return SALT

def generar_key_fernet (password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256 (),
        length=32,
        salt=base64.b64decode(salt),
        iterations=480000
    )

    key_derive = kdf.derive (password)

    key_fernet = base64.urlsafe_b64encode (key_derive)
    return key_fernet


def encriptar (password, message, salt):
    key = generar_key_fernet (password, salt)
    f = Fernet(key)

    message = f.encrypt (message.encode ('utf-8'))
    return message

if __name__ == '__main__':
    contar = 0
    SALT = ""
    password = "fulano2001".encode ('utf-8')
    for _ in range (4):
        message = input ("Message: ")
        if contar == 0:
            SALT = Generar_salt ()
        
        result = encriptar (password, message, SALT)
        print (result)