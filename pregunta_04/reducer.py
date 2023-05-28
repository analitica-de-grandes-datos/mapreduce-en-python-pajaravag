# Pablo Andres
import sys
# from datetime import datetime

# if __name__ == "__main__":
#     data = []

#     for line in sys.stdin:
#         row = line.strip()
#         row = row.split('\t')
#         data.append(row)

#     arrangement = sorted(data, key = lambda x: datetime.strptime(x[1], '%Y-%m-%d'))

#     for item in arrangement:
#         sys.stdout.write('{}   {}   {}\n'.format(item[0], item[1], item[2]))

# Inicializar el diccionario para almacenar los conteos de credit_history
credit_counts = {}

# Leer los datos de la entrada estándar
for line in sys.stdin:
    # Eliminar espacios en blanco y dividir la línea en clave y valor
    credit_history, count = line.strip().split('\t')

    # Convertir el conteo a entero
    count = int(count)

    # Incrementar el contador para el tipo de credit_history actual
    if credit_history in credit_counts:
        credit_counts[credit_history] += count
    else:
        credit_counts[credit_history] = count

# Imprimir los resultados

for credit_history in sorted(credit_counts.keys()):
    count = credit_counts[credit_history]    
    sys.stdout.write("{},{}\n".format(credit_history, count))