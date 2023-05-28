import sys

if __name__=="__main__":

    for line in sys.stdin:

        row = line.strip().split('\t')

        for item in row[1]:

            word = item.strip().split(',')

            if len(word) == 1:
                sys.stdout.write("{}\t{}\n".format(word[0], row[0]))