import sys

if __name__ == '__main__':

    mes_count = {}

    for line in sys.stdin:
        row = line.strip()

        mes, count = row.split('\t')
        count = int(count)
        mes = str(mes)

        if mes in mes_count:
            mes_count[mes] += count
        else:
            mes_count[mes] = count
    
    for mes in sorted(mes_count):
        count = mes_count[mes]
        sys.stdout.write("{}\t{}\n".format(mes, count))

