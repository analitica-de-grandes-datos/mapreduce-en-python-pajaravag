import sys

if __name__=="__main__":

    for line in sys.stdin:
        row = line.strip().split('   ')
        sys.stdout.write("{}\t{}\t{}\n".format(row[0], row[1], row[2]))