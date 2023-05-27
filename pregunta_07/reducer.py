import sys
if __name__ == "__main__":
    data = []

    for line in sys.stdin:
        row = line.strip()
        row = row.split('\t')
        data.append(row)
    
    arrangement = sorted(data, key = lambda x: (x[0], int(x[2])))

    for item in arrangement:
        sys.stdout.write('{}   {}   {}\n'.format(str(item[0]), str(item[1]), item[2]))