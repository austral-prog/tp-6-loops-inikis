# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    todos_elem=[]
    for lista in matrix:
        for elem in lista:
            todos_elem.append(elem)

    return todos_elem

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista_suma=[]
    for lista in matrix:
        suma=0
        for elem in lista:
            suma+=elem

        lista_suma.append(suma)

    return lista_suma


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    suma_col=[]

    lista_columnas=[]
    
    #todas las filas tienen la misma longitud. esto nos da la cant de columnas
    cant_columnas=len(matrix[0])
    for cant in range(cant_columnas):
        lista_columnas.append([])

    for lista in matrix:
        for columna, numero in enumerate(lista):
            lista_columnas[columna].append(numero)
    
    for columnas in lista_columnas:
        suma=0
        for columna in columnas:
            suma+=columna
        suma_col.append(suma)

    return suma_col
