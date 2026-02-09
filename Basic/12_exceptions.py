
# Excepción base: try except

"""
Sintaxis

try:
    bloque de codigo
except:  -> Especifca el tipo de error a capturar
else: -> en caso no se ejecute el try/except
finally: -> se ejecuta siempre si o si
"""



numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)


## ------------------ Lanzar una excepcion -> raise <- --------------------

# La raisepalabra clave se utiliza para generar una excepción.
# Puede definir qué tipo de error generar y el texto que se le mostrará al usuario.

# Genera un TypeError si x no es un entero:
x = "hello"

if not type(x) is int:
  raise TypeError("Sólo se permiten números enteros")


# raise  ->  permite lanzar una excepcion

x = -1

if x < 0:
  raise Exception("Lo sentimos, no hay números por debajo de cero.")


x = "hello"

if not type(x) is int:
  raise TypeError("Sólo se permiten números enteros")



## ----------------------- Creando excepciones propias ---------------------

class AutenticateError (Exception):
    def __init__(self, email):
        # dentro del __ini__ (AQUI VA EL MENSAJE UE DESEAMOS QUE SALGA)
        super().__init__(f"Error invalido {email}")
        self.email = email

    
    def validacion_email(self):
        pass

# ejemplo ----------

class PasswordCortaError(Exception):
    def __init__(self, password):
        self.password = password
        super().__init__(f"La contraseña '{password}' es demasiado corta")

def validar_password(password):
    if len(password) < 6:
        raise PasswordCortaError(password)

    return "Contraseña válida"


try:
    resultado = validar_password("123")
    print(resultado)

except PasswordCortaError as error:
    print("Error detectado")
    print(error)

# ejemplo ---------------------------------


class AuthenticateError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f"Email inválido: {email}")

    def dominio_valido(self):
        dominios_validos = ["@gmail.com", "@hotmail.com", "@undac.edu.pe"]
        return any(self.email.endswith(d) for d in dominios_validos)

def login(email):
    dominios_validos = ["@gmail.com", "@hotmail.com", "@undac.edu.pe"]

    if not any(email.endswith(d) for d in dominios_validos):
        raise AuthenticateError(email)


try:
    login("usuario@fake.com")
except AuthenticateError as e:
    print(e)
    print("Email:", e.email)
    print("Dominio válido:", e.dominio_valido())

"""
🧠 JERARQUÍA DE EXCEPCIONES (IMPORTANTE)

Todas heredan de:

BaseException
 └── Exception
     ├── ValueError
     ├── TypeError
     ├── IndexError
     ├── FileNotFoundError


👉 Nunca captures BaseException
"""


"""
   CONSIDERACIONES EN LAS EXCEPCIONES AVANZADOS

✔ Tus validaciones NO deben estar en la excepción
✔ Tus print() NO deben estar en la excepción
✔ Las excepciones NO validan
✔ Las excepciones solo informan del error
✔ La lógica valida → lanza
✔ El controlador captura → muestra

🧩 Analogía (muy clara)

Piensa en una excepción como:

🚨 Una alarma de incendio
❌ La alarma no apaga el fuego
❌ La alarma no llama a los bomberos
❌ La alarma no imprime mensajes
"""