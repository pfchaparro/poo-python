import random

def ordenamiento_de_insercion(lista):
    for i in range (len(lista)-1):
        if lista[i+1] < lista[i]:
            mover(lista,i+1)

    return lista

def mover(lista, p):
    v = lista[p]
    j = p

    while j > 0and v < lista[j-1]:
        lista[j] = lista[j-1]
        j -= 1

        lista[j] = v


if __name__ == '__main__':
    tamano_de_la_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0,100) for i in range (tamano_de_la_lista)] 
    print(lista)

    lista_ordenada = ordenamiento_de_insercion(lista)
    print(lista_ordenada)