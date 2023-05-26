import sys
if __name__ == "__main__":
    data = []

    for line in sys.stdin:
        row = line.strip()
        row = row.split('\t')
        data.append(row)
    
    arrangement = sorted(data, key = lambda x: (x[1]))

    for item in arrangement:
        sys.stdout.write('{},{}\n'.format(item[0], item[1]))
