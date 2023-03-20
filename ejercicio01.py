def encontrar_maxcomdiv(numa, numb):
    divisores=[]
    comunesdiv=[]
    for i in range(1, max(numa,numb), +1):
        if max(numa,numb) % i == 0:
            divisores.append(i)
    for i in divisores:
        if min(numa,numb) % i == 0:
            comunesdiv.append(i)
    return max(comunesdiv)
print(encontrar_maxcomdiv(18, 12))