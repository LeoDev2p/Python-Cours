"""
Documentacion
-> https://argon2-cffi.readthedocs.io/en/stable/api.html
"""


from argon2 import PasswordHasher

ph = PasswordHasher(
    time_cost=3,  # Cuántas vueltas / capas de mescla q' tendra la contraseña (CPU)
    memory_cost=65536,  # 64MB de RAM ((cantidad de ram a usar en cada vuelta) (128 MB -> 131072 kb)
    parallelism=1,  # cantidad de hilos/nucelos a usar
    hash_len = 32, # longitud del hash resultante
    salt_len = 16, # longitud del salt generado (aleatorio)
    encoding = 'utf-8' # codificacion del hash resultante (utf-8, latin-1, ascii
)

# OJO: el tiempo del time_cst debe eestar entre 200 y 500 ms, para que el usuairo no espere mucho

hash = ph.hash("Contraseña")  # True
print(hash)

# * argon2.exceptions.HashingError – Si el hash falla.
# * Lanza un error durante la creacion dle hash (memoria, parametro invalido, nucleos)

hash_verify = ph.verify(hash, "contraseña")  # True

"""
argon2.exceptions.VerificationError – Si la verificación falla por otros motivos.

argon2.exceptions.VerifyMismatchError – Si la verificación falla porque el hash no es válido para la contraseña .

argon2.exceptions.InvalidHashError – Si el hash es tan claramente inválido que no se puede pasar a Argon2.
"""

ph.check_needs_rehash(hash)
# devuelve False si la clave sige siendo fuerte
# devuelve True si requiere ya de cambiar la contraseña, por (actualizacion de la libreria / modificacion en la configuracion)
