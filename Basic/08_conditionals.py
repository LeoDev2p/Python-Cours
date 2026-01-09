
### Conditionals ###

"""
if expresion:                --> Realiza la primera evaluación
    bloque de codigo / condicion                
elif expresion:               --> si el if es falso realiza la evaluacion
    bloque de codigo  / condicion
else:                          --> Se ejecuta si las condiciones anteriores son falsas
    bloque de codigo / ocndicion
"""

# if --> Evalua una condicion

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# ilif  -> Si el if no es falso entra al elif (puede haber tanto como desees)
# else  -> Esta condicion se cumple siempre y cuando las anteriores no son verdaderas

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")



## Abreviaturas en las condiciones siempre y cuando sean cortas

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


###  Match y case  

"""
match expression:    --> Se evalua una sola vez
  case x:                 --> Si el valor de la expresion coincide con el case se ejecuta
    code block
  case y:
    code block
  case z:
    code block
"""

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:        # poner "_"  cuando no haya otras coincidencias y que se ejecute
    print("Looking forward to the Weekend")


# cuando queremos evaluar mas de una coincidencia
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# Match con condiciones
x = 6
match x:
    case n if n > 5 and n < 10:
        print("entre 6 y 9")