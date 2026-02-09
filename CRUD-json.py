import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ruta_txt = BASE_DIR / "Intermediate" / "my_file.json"


def file_db_read ():
    with  open (ruta_txt, "r", encoding="utf-8") as file:
        try:
            data = json.load (file)
        except json.JSONDecodeError as e:
            msg = f"Error: {e.msg}, {e.lineno}, {e.colno}"
            raise json.JSONDecodeError (msg)

        
        return data

def file_db_save (data):
    with open (ruta_txt, "w", encoding="utf-8") as filed:
        json.dump (data, filed, indent=4)


def validate_Student (Cod_student, db):
    return  Cod_student not in db.keys ()


def Add_Studen (query):
    # query = [codig, nombre, apellido, state]
    db = file_db_read () or {}
    if validate_Student (query, db):
        db[query[0]] = {
            "Name": query[1],
            "Lastname": query[2],
            "Promedio": [],
            "State": query[3],
            "cursos": {
                "Matematica": [],
                "Comunicacion": [],
                "Historia": []
            }
        }
        

        file_db_save (db)

        return query[1] + query[2]
    
    return "Estudiante ya existe"


def Update_student_Nota (Cod_student, curso, notas):
    if not validate_Student (Cod_student):
        db = file_db_read ()
        try:
            db[Cod_student]["cursos"][curso].extend ([notas])
        except KeyError as k:
            raise KeyError (f"Error clave incorrecta:  {curso}")
        
        file_db_save (db)

        return (db[Cod_student]["Name"], notas)

def Delete_Student (Cod_student):
    if not validate_Student (Cod_student):
        db = file_db_read ()
        eliminate = db.pop (Cod_student)

        file_db_save (db)

        return eliminate

def Mostrar_alumnos ():
    db = file_db_read ()
    print ("-"*66)
    print ("N°  |  Alumno  | Matematica  | Comunicacion |  Historia | Promedio")

    cont = 0
    for cod in db:
        mate = round (sum (db[cod]["cursos"]["Matematica"]) / 4, 2)
        mate_str = f"{mate:.2f}"

        comu = round (sum (db[cod]["cursos"]["Comunicacion"]) / 4, 2)
        histo = round (sum (db[cod]["cursos"]["Historia"]) / 4, 2)

        abreviatura = db[cod]["Name"].split (" ") + db[cod]["Lastname"].split (" ")
        a = [k[0] for k in abreviatura]

        print (f"{cont}   |   {"".join(a)}   |    {mate:05.2f}    |    {comu:05.2f}     |    {histo:05.2f}  |   {round((mate+comu+histo)/3, 2)}")
        cont += 1


    print ("-"*66)

def validaar_codigo (cod):
    return len(cod) == 8




if __name__ == "__main__":
    while True:
        print ("""
            1. Agregar estudiante
            2. Actualizar notas x curso
            3. Mostrar alumnos con notas
            4. Eliminar estudiante
            5. Salir
        """)

        try:
            opcion = int (input ("OPcion_: "))
        except ValueError as e:
            print (e)
            continue

        match opcion:
            case 1:
                while True:
                    # query = [codig, nombre, apellido, state]
                    try:
                        codigo = input ("Codigo (0: terminar): ")
                        if codigo == "0":
                            break

                        if not validaar_codigo (codigo):
                            print ("Codigo de estudiante invalido")
                            continue

                        nombre = input ("Nombre: ")
                        apellido = input ("Apellido: ")
                        estado = input ("Estado (True/False): ")
                    except ValueError as e:
                        print (e)
                        continue

                    query = (codigo, nombre, apellido, estado)

                    print ("\n", Add_Studen (query), "\n")
            case 2:
                while True:
                    # query = [codig, nombre, apellido, state]
                    try:
                        codigo = input ("Codigo (0: terminar): ")
                        if codigo == "0":
                            break

                        if not validaar_codigo (codigo):
                            print ("Codigo de estudiante invalido")
                            continue

                        curso = input ("Curso: ").capitalize ()
                        for _ in range (4):
                            nota = float (input ("Nota (0/20): "))
                            if nota == -1:
                                break

                            Update_student_Nota (codigo, curso, nota)
                    except ValueError as e:
                        print (e)
                    except KeyError as k:
                        print (k)
                    except json.JSONDecodeError as jd:
                        print (jd.msg, jd.lineno, jd.colno)
                    
            case 3:
                try:
                    Mostrar_alumnos ()
                except json.JSONDecodeError as e:
                    print (e.msg, e.lineno, e.colno)
            case 4:
                try:
                    codigo = input ("Codigo: ")
                    
                    if not validaar_codigo (codigo):
                        print ("Codigo de estudiante invalido")
                        continue

                    Delete_Student (codigo)
                except ValueError as e:
                    print (e)
                except json.JSONDecodeError as jd:
                    print (jd.msg, jd.lineno, jd.colno)

            case 5:
                break
            case _:
                print ("Opcion no disponible")

           

