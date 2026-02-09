
"""
Docstring for Hello-Python.Basic.14. testear.debugear

Depurar con pdb

 ---------------- comandos claves ----------------------

Comando	      Qué hace
l	          ver código
n	          siguiente línea
s	          entrar a función
r             volver
p query	      ver variable
p query[2]	  ver email
p data_user	  ver BD
c	          continuar
q	          salir
"""

# ejemplo 
import pdb


def Login(self, query):
    pdb.set_trace()  # 🔴 Punto de interrupción

    if self.Validar_usuario(query[0]):
        try:
            if self.Validar_email(query[2]) and self.Validar_password(query[3]):
                data_user = BD_Usuarios.Leer()[query[0]]

                if query[2] != data_user["email"] or query[3] != data_user["password"]:
                    return None

                self.Estado = True
                self.nombre_usuario = query[1]
                self.role = query[4]

        except AutenticacionError as a:
            print("Error:", a)

    else:
        return False

    return True

"""
p query
p query[2]
p self.Validar_email(query[2])
n
"""

# --------------------- LOGGING -----------------------------

"""
Depurar con logging (forma profesional)
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(message)s"
)

def Login(self, query):
    logging.debug(f"Intento de login con DNI: {query[0]}")

    if self.Validar_usuario(query[0]):
        try:
            logging.debug("Usuario encontrado en BD")

            self.Validar_email(query[2])
            self.Validar_password(query[3])

            data_user = BD_Usuarios.Leer()[query[0]]
            logging.debug(f"Datos usuario BD: {data_user}")

            if query[2] != data_user["email"]:
                logging.warning("Email incorrecto")
                return None

            if query[3] != data_user["password"]:
                logging.warning("Password incorrecto")
                return None

            self.Estado = True
            self.nombre_usuario = query[1]
            self.role = query[4]

            logging.info("Login exitoso")
            return True

        except AutenticacionError as a:
            logging.error(f"Error autenticación: {a}")
            return False

    logging.warning("Usuario no registrado")
    return False


"""
QUE VERAS EN CONSOLA 

DEBUG | Intento de login con DNI: 123
DEBUG | Usuario encontrado en BD
ERROR | Error autenticación: Email inválido

"""