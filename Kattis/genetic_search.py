#!/usr/bin/python
import re


def main():
    fin = open('sample.in', 'r')
    chars = set('AGCT')

    for line in fin:
        if not any((c in chars) for c in line):
            exit()
        strList = line.split()
        if 2 <= len(strList[0]) <= len(strList[1]) <= 100:
            t1 = t2 = t3 = 0
            s = set()
            t1 = count(strList[1], strList[0])
            for n in range(len(strList[0])):
                word = strList[0][:n] + strList[0][n + 1:]
                if word in s:
                    continue
                s.add(word)
                t2 += count(strList[1], word)

            s.clear()
            for n in range(len(strList[0]) + 1):
                for c in chars:
                    word = strList[0][:n] + c + strList[0][n:]
                    if word in s:
                        continue
                    s.add(word)
                    t3 += count(strList[1], word)
            print t1, t2, t3


def count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in xrange(0, string_size - substring_size + 1):
        if string[i:i + substring_size] == substring:
            count += 1
    return count

if __name__ == "__main__":
    # start_time = time.time()
    main()
    # print("\n%s seconds" % (time.time() - start_time))
