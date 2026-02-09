
import secrets
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

salt = secrets.token_bytes(16)
print (f"salt={salt}")

satl_legible = base64.b64encode(salt).decode ('utf-8')
print (satl_legible)

contrasena = "como_estas".encode('utf-8')

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000
)

kewy_raw = kdf.derive (contrasena)
print (kewy_raw)

fernet_key = base64.urlsafe_b64encode(kewy_raw)
print (fernet_key)