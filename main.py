def buscar_repetidos(lista,valor):
    return valor in lista

def busqueda(lista,valor):
    inicio = 0
    fin = len(lista) - 1
    while fin >= inicio:
        medio = (fin + inicio) // 2 
        if lista[medio] == valor:
            return True 
        if fin == inicio:
            break
        if lista[medio] > valor:
            fin = medio -1
        else:
            inicio = medio + 1
    return False                  