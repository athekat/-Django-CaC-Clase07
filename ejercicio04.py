def contar_palabras(frase):
    listapalabras = frase.split()
    frecuencia = []
    for palabra in listapalabras:
        frecuencia.append(listapalabras.count(palabra))
    return (dict(zip(listapalabras, frecuencia)))


def palabra_mas_repetida(frecuencia):
    max_frecuencia = max(frecuencia.values())
    for palabra, freq in frecuencia.items():
        if freq == max_frecuencia:
            return (palabra, freq)


cadena = input("Ingrese una cadena de caracteres: ")
diction = contar_palabras(cadena)
print(palabra_mas_repetida(diction))
