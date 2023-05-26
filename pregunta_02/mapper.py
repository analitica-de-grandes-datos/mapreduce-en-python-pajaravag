import sys

if __name__=="__main__":

    for line in sys.stdin:
        ch = line.strip()
        ch = ch.split(',')
        sys.stdout.write("{}\t{}\n".format(ch[3], ch[4]))
