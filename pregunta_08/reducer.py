import sys

if __name__ == '__main__':

    word_count = {}
    word_times = {}

    for line in sys.stdin:
        row = line.strip()

        word, times, count = row.split('\t')
        count = float(count)
        word = str(word)
        times = float(times)

        if word in word_count:
            word_count[word] += count
            word_times[word] += times
        else:
            word_count[word] = count
            word_times[word] = times
    
    for word in sorted(word_count):
        counter = word_count[word]
        average_word = word_count[word] / word_times[word]
        sys.stdout.write("{}   {}   {}\n".format(word, counter, average_word))