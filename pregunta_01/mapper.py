# Oscar es el Llanerazo
#
import sys
if __name__ == "__main__":


    for line in sys.stdin:
        ch = line.strip()
        ch = ch.split(',')
        sys.stdout.write("{}\t1\n".format(ch[2]))
