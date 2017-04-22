#!/usr/bin/python

from sys import maxint


def main():
    target = int(raw_input("Target: "))
    values = [int(i) for i in raw_input("Values: ").split()]

    print closest_num(target, values)

    return 0


def closest_num(target, values):
    diff = maxint
    num = 0
    for n in values:
        if diff > abs(n - target):
            diff = abs(n - target)
            if diff is not 0:
                num = n
            else:
                return min(s for s in values)
    return num


if __name__ == "__main__":
    # start_time = time.time()
    main()
    # print("\n%s seconds" % (time.time() - start_time))
