cadena = input("Ingrese una cadena de caracteres: ")
listapalabras = cadena.split()
frecuencia = []
for palabra in listapalabras:
    frecuencia.append(listapalabras.count(palabra))
print(dict(zip(listapalabras,frecuencia)))
