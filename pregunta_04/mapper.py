# import sys
# if __name__ == "__main__":

#     for line in sys.stdin:
#         row = line.strip()
#         row = row.split('   ')
#         sys.stdout.write('{}\t{}\t{}\n'.format(row[0], row[1], row[2]))

import sys

for row in sys.stdin:
    elementos = row.strip().split(",")
    campos = elementos[0]
    column = campos.split("   ")
    linea = column[0]
    #linea = ",".join(column)
    sys.stdout.write((linea+"\t1\n"))