import sys
if __name__ == "__main__":
    data =[]

    for line in sys.stdin:
        row = line.strip()
        row = row.split('   ')
        
        sys.stdout.write('{}\t1\n'.format(row[1].split('-')[1]))