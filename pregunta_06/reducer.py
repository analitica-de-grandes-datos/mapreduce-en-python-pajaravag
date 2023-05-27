import sys

if __name__ == '__main__':

    min_value, max_value = {}, {}

    for line in sys.stdin:
        key, value = line.strip().split('\t')
        value = float(value)

        if key in max_value:
            max_value[key] = max(max_value[key], value)
            min_value[key] = min(min_value[key], value)
        
        else:
            max_value[key] = value
            min_value[key] = value

    for key in sorted(max_value.keys()):
        max_val = max_value[key]
        min_val = min_value[key]   
        sys.stdout.write('{}\t{}\t{}\n'.format(key, max_val, min_val))