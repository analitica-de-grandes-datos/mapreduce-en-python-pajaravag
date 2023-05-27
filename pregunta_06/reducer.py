import sys

if __name__ == '__main__':

    curkey = None
    total = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            if val >= total:
                total = val
            
            else:
                total = total

        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = val

    sys.stdout.write("{}\t{}\n".format(curkey, total))