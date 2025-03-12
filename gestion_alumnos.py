
import json  #Importando nuestro archivo Json 
 
def cargar_alumnos(ruta_archivo): #Creando una funcion para cargar los datos de los alumnos
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)
                            
def buscar_alumno(alumnos, nombre): #Segunda funcion para buscar alumnos del archivo json
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower(): #Si se pone mayusculas o minusculas igual se busque 
            return alumno
    return None 

if __name__ == "__main__":   #Hacer correr nuestor archivo 
    ruta = "Laboratorio6/alumnos.json" #Ruta del archivo Json para la busqueda 
    alumnos = cargar_alumnos(ruta)
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")

    resultado = buscar_alumno(alumnos, nombre_buscar)  #Resultado de la busqueda
    if resultado:
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")