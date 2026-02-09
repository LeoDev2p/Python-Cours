from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import secrets
import base64

# 1. Creamos la semilla de 16 bytes
salt_crudo = secrets.token_bytes(16)

# 2. Hacemos legible el salt
salt_legible = base64.b64encode(salt_crudo).decode ('utf-8')
print (salt_legible)

# 3. Preparar los datos en bytes (PBKDF2 solo entiende bytes)
password_bytes = "mi_contraseña_super_secreta".encode('utf-8')
salt_bytes = base64.b64decode(salt_legible) # Decodificamos el que tenías guardado

# 2. Configurar la "máquina" (KDF)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(), # Usamos SHA256 como motor de hash
    length=32,                  # ¡IMPORTANTE! Fernet exige exactamente 32 bytes
    salt=salt_bytes,            # El salt que recuperamos
    iterations=480000,          # Recomendado por OWASP (hace que sea lento para hackers)
)

# 3. Derivar la llave (Aquí ocurre la magia)
# Esta función "estira" la contraseña y genera 32 bytes aleatorios basados en ella
key_raw = kdf.derive(password_bytes)

# 4. Formatear para Fernet
# Fernet no acepta los bytes crudos, necesita que estén en "Base64 seguro para URL"
fernet_key = base64.urlsafe_b64encode(key_raw)

print(f"Tu llave de Fernet es: {fernet_key.decode()}")
