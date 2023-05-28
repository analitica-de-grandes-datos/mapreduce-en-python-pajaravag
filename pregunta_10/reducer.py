import sys
from itertools import groupby

# Inicializar una lista vacía para almacenar sublistas
list_of_lists = []

# Leer líneas de entrada de sys.stdin
for line in sys.stdin:
    # Eliminar el carácter de nueva línea de la línea
    line = line.replace('\n', '')
    
    # Dividir la línea en elementos utilizando el separador '\t' y crear una nueva lista
    new_list = [elem for elem in line.split("\t")]
    
    # Agregar la nueva lista a la lista de listas
    list_of_lists.append(new_list)
    
    # Convertir el segundo elemento de cada sublista en un entero
    for n in range(len(list_of_lists)):
        list_of_lists[n][1] = int(list_of_lists[n][1])

# Ordenar la lista de listas por el primer elemento y luego por el segundo elemento
list_of_lists = sorted(list_of_lists, key=lambda x: (x[0], x[1]))

# Agrupar las sublistas por el primer elemento y crear una nueva lista de tuplas
nuevalista = [(k, list([e[1] for e in g])) for k, g in groupby(list_of_lists, lambda x: x[0])]

for pareja in nuevalista:
    sys.stdout.write("{}\t{}\n".format(str(pareja[0]), str(pareja[1]).replace('[','').replace(']', '').replace(' ','')))