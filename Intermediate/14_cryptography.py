"""
Documentacion
-> https://cryptography.io/en/latest/fernet/
"""
from cryptography.fernet import Fernet

# creamos la llave solo una vez guardarlo
key = Fernet.generate_key()  # devulve una llave en byte b'hhdjsseiurieur....' 32 bytes = 256 bits

# Instanciamos Fernet con nuestra clave maestra
f = Fernet(key)


def encrypt_data(data: str) -> bytes:
    """Encripta un string de texto y devuelve bytes encriptados."""
    # Fernet trabaja con bytes, así que primero convertimos el string a bytes (utf-8)
    encoded_data = data.encode("utf-8")
    token = f.encrypt(encoded_data)
    return token


# TypeError – Esta excepción se genera si data no es bytes.


def decrypt_data(token: bytes) -> str:
    """Desencripta los bytes y devuelve el string original."""
    # Desencriptamos y decodificamos a string
    decrypted_data = f.decrypt(token)
    original_string = decrypted_data.decode("utf-8")
    return original_string


"""
cryptography.fernet.InvalidToken : si la Llave es incorrecta, El Token ha sido manipulado, o el Token ha expirado con el parametro ttl (si se usó un tiempo de vida), Tocken mal formado

TypeError – Esta excepción se genera si token no es bytes o str.
"""
