import sqlite3, datetime

print("**** Programa para insertar registro  en la tabla test ****")

cadena_texto = input("Introduzca una cadena de texto: ")
entero = input("Introduzca un nuemro entero: ")
decimal = input("Introduce un numero decimal: ")

try: entero = int(entero)
except ValueError:
    print(entero, "no es un n ´´un numero entero")
    exit()

try: decimal = float(decimal) or int (decimal)
except ValueError: 
    print (decimal, "no es un número decimal")
    exit()

#Establecer la conexión
conexion = sqlite3.connect("sqlite3/test.sqlite3")

# selecionar el cursor para iniciar la consulta 
consulta = conexion.cursor()

#Valor de los argumento 
argumentos = (cadena_texto, entero, decimal, datetime.date.today())

sql = """
INSERT INTO TEST (cadena_testo, entero, decimal, fecha)
VALUES (?, ?, ?, ?)
"""

#Realizar la consulta 
if (consulta.execute(sql, argumentos)):
    print("Registro guardado con exito")
else: ("Ha ocurrido un error al guardar el registro")

#terminamos la consulta 
consulta.close()
