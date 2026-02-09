
### ----------------- PROGRAMACIÓN ORIENTADA A OBJETOS (POO) -----------------

"""
Clase:  El molde o plantilla para crear objetos
Objeto: Una unidad que junta datos + comportamiento
"""


# self, nos permite acceder a metodos o variables dentro de la clase

class Person:
  # __init__  : es el constructor de la clase
  def __init__(self, name, age = 20):
    # Estos son propiedades de la clase
    self.name = name
    self.age = age

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Isaias", 23)
p1.name = "Cesar"  # Modificando el valor de una propiedad
print (p1.age)  # accediendo al valor de una propiedad
p1.welcome()

# ejemplo -----

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar (self, student):
        self.name = student
        if self.nombre == "Isaias":
            print (f"BUenos dias {student}")
    

person1 = Persona ("Isaias", 23)
print (person1.edad)
print (person1.nombre)
person1.saludar ("Kriptom")
print (person1.name)

# Creando clases sin constructor ni codigo

class Person:
  pass

p1 = Person()
p1.name = "Isaias"
p1.age = 25
p1.Pais = "Peru"

print(p1.name)
print(p1.age)
print (p1.Pais)

# propiedades de objeto vs propiedades de clase

class Person:
  # pertenecen a la clase misma (propiedades de clase) y son compartidas por todos los objetos:
  species = "Human" # Class property

  def __init__(self, name):
    # pertenecen a cada objeto (propiedades de instancia).
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# ------------------------- METODOS DE CLASE ------------------------------

# __str__  : method is a special method that controls what is returned when the object is printed:

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # funcion que si o si devuelve en primera instancia
    def __str__(self):
        return f"Mi nombre es {self.nombre} y mi edad es {self.edad}"
    
    def saludar (self, student):
        self.name = student
        if self.nombre == "Isaias":
            print (f"BUenos dias {student}")
    

person1 = Persona ("Isaias", 23)
print (person1)  # Imprime el __str__
print (person1.edad)
print (person1.nombre)
person1.saludar ("Kriptom")
print (person1.name)


### ********************* HERENCIA DE CLASES *************************
"""
La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Clase hija : Hereda todas las propiedades y funcionalidades de la clase padre

class Student(Person):
    # Inicializando el constructor podemos personalizar las propiedades de la clase hija en referencia a la del padre
    def __init__ (self, name, lastname, country):
       # Apuntamos a la clase padre, pasandole los datos de su constructor
       Person.__init__ (self, name, lastname)

       self.name = name
       self.lastname = lastname
       self.country = country

s1 = Student ("Isaias", "Quintana", "Peru")
print (s1.name)
s1.printname ()

# ------------------------------------------------------------------------

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
    def __init__ (self, name, lastname, country):
       # La funcion super (), nos permite ya no usar el nombre de la clase padre
       super ().__init__ (name, lastname)

       self.country = country

    def welcome (self):
       return f"Bienvenido a la clase {self.firstname} {self.lastname}"

s1 = Student ("Isaias", "Quintana", "Peru")
print (s1.firstname)
s1.printname ()
print (s1.welcome ())


## ************************** POLIMORFISMO  ************************

"""
El polimorfismo se utiliza a menudo en los métodos de clase, donde podemos tener varias clases con el mismo nombre de método.

Por ejemplo, digamos que tenemos tres clases: Car, Boat, y Plane, y todas tienen un método llamado move():
"""

class Car:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


# otro ejemplo polimorfismo con herencias ---------------------------------

class Vehicle:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.marca)
  print(x.modelo)
  x.move()

## ---------------------- ENCAPSULAMIENTO -----------------------------

class Person:
  def __init__(self, name, age):
    self._name = name  # protegido ( solo indica tener cuidado)
    self.__age = age # privado

p1 = Person("Isaias", 25)
print(p1._name)
# print(p1.__age) # da error
print (p1._Person__age)

# ejemplo encapsulamiento metodos

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error