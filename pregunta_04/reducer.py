# Pablo Andres
import sys
from datetime import datetime

if __name__ == "__main__":
    data = []

    for line in sys.stdin:
        row = line.strip()
        row = row.split('\t')
        data.append(row)

    arrangement = sorted(data, key = lambda x: datetime.strptime(x[1], '%Y-%m-%d'))

    for item in arrangement:
        sys.stdout.write('{}\t{}\t{}\n'.format(item[0], item[1], item[2]))