
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        row = line.strip()
        row = row.split(',')
        sys.stdout.write('{}\t{}\n'.format(row[0], int(row[1])))
