import sys

if __name__ == "__main__":

    for line in sys.stdin:
        row = line.strip()
        row = row.split('   ')
        sys.stdout.write('{}\t1\t{}\n'.format(row[0], row[2]))