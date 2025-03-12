import unittest  
from gestion_alumnos import buscar_alumno #Del archivo gestion_alumnos se importa su metodo de buscar_alumno

class TestGestionAlumnos(unittest.TestCase): #Clase del archivo gestion_alumnos_test

    def setUp(self): #Funcion de la clase TestGestionAlumnos 
        self.alumnos = [{"nombre": "Ana","edad":20,"carrera":"Ingenieria"},
                        {"nombre": "Luis","edad":22,"carrera":"Matematicas"},
                        {"nombre": "Maria","edad":21,"carrera":"Fisica"}]  #Datos para verificar si hay errores

    def test_buscar_alumno_existente(self):   #Buscador de errores 
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nombre"], "Ana")

    def test_buscar_alumno_inexistente(self): #Buscador de errores
        resultado = buscar_alumno(self.alumnos, "Carlos")
        self.assertIsNone(resultado)

if __name__ == "__main__":  #Metodo principal
    unittest.main()