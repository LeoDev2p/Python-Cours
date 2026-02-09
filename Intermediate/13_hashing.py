"""
Documentacion
-> https://argon2-cffi.readthedocs.io/en/stable/api.html
"""


from argon2 import PasswordHasher

ph = PasswordHasher(
    time_cost=3,  # Cuántas vueltas / capas de mescla q' tendra la contraseña (CPU)
    memory_cost=15360,  # 15MB de RAM ((cantidad de ram a usar en cada vuelta)
    parallelism=1,  # cantidad de hilos/nucelos a usar
)

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
