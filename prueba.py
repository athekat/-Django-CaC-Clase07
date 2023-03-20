class Persona():
    def __init__(self, pNombre ="", pEdad = 0, pDni = ""):
        self.__nombre = pNombre
        self.__edad = pEdad
        self.__dni = pDni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, pNombre):
        if type(pNombre) != str:
            raise ValueError("El nombre debe ser un string.")
        self.__nombre = pNombre

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, pEdad):
        if type(pEdad) != int or pEdad < 0:
            raise ValueError("La edad debe ser un número válido.")
        self.__edad = pEdad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, pDni):
        if type(pDni) != str or len(pDni) != 8:
            raise ValueError("DNI no válido.")
        self.__dni = pDni

    def mostrar(self):
        return f"Este individuo se llama {self.nombre}, tiene {self.edad} años y su documento es {self.dni}."
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

persona_01 = Persona("Pepe", 26, "35368897") #¿Está ok esto? ¿O debo hacerlo como se hizo en persona_02?
print(persona_01.mostrar())
print(persona_01.es_mayor_de_edad())
print("-----------------------")
persona_02 = Persona()
persona_02.nombre ="Juan"
persona_02.edad = 17
persona_02.dni ="40567218"
print(persona_02.mostrar())
print(persona_02.es_mayor_de_edad())