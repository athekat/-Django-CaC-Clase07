class Persona():
    def __init__(self, pNombre="", pEdad=0, pDni=""):
        self.__nombre = pNombre
        self.__edad = pEdad
        self.__dni = pDni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, pNombre):
        if isinstance(pNombre) != str:
            raise ValueError("El nombre debe ser un string.")
        self.__nombre = pNombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, pEdad):
        if isinstance(pEdad) != int or pEdad < 0:
            raise ValueError("La edad debe ser un número válido.")
        self.__edad = pEdad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, pDni):
        if isinstance(pDni) != str or len(pDni) != 8:
            raise ValueError("DNI no válido.")
        self.__dni = pDni

    def mostrar(self):
        return f"Este individuo se llama {self.nombre}, tiene {self.edad} años y su documento es {self.dni}."

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta():
    def __init__(self, pTitular=Persona(), pCantidad=0):
        if isinstance(pTitular, Persona):
            self.__titular = pTitular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona.")
        self.__cantidad = pCantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, pTitular):
        if isinstance(pTitular, Persona):
            self.__titular = pTitular
        else:
            print("Error: El titular debe ser una instancia de la clase Persona.")

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, pCantidad):
        if isinstance(pCantidad) != float:
            print("Numero no válido")
        else:
            self.__titular = pCantidad

    def mostrar(self):
        return (f"El titular de la cuenta es {self.titular.nombre} y su saldo es de {self.cantidad}.")

    def ingresar(self, nCantidad):
        if nCantidad < 0:
            print("Ingrese un número positivo.")
        else:
            self.__cantidad += nCantidad

    def retirar(self, nCantidad):
        if nCantidad < 0:
            print("Ingrese un número positivo.")
        else:
            self.__cantidad -= nCantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, pBonificacion):
        self.__bonificacion = pBonificacion

    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad <= 26

    def retirarcj(self, pCantidad):
        if self.es_titular_valido():
            super().retirar(pCantidad)
        else:
            print("Usuario no autorizado para retirar")

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular.nombre}\nCantidad: {self.cantidad}\nBonificación: {self.bonificacion}%"


persona_01 = Persona("Juan", 27, "35697412")
cuenta_01 = CuentaJoven(persona_01, 300)
cuenta_01.ingresar(800)
cuenta_01.retirarcj(1100)
print(cuenta_01.mostrar())
