import sys

if __name__ == "__main__":
    data = []

    for line in sys.stdin:
        row = line.strip()
        row = row.split('\t')
        data.append(row)

    arrangement = sorted(data, key = lambda x: int(x[2]))

    for item in arrangement[:6]:
        sys.stdout.write('{}   {}   {}\n'.format(item[0], item[1], item[2]))