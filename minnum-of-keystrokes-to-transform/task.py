#!/usr/bin/python
import time
import difflib


def main():
    while True:
        orig_word = raw_input("Original word: ")
        if not orig_word:
            break
        new_word = raw_input("New word: ")
        if not new_word:
            break
        analyze_keystrokes(orig_word, new_word)


def analyze_keystrokes(orig, new):
    """Based on overlap of strings."""
    overlap = 0

    overlaps = difflib.SequenceMatcher(None, orig, new).get_matching_blocks()
    for o in overlaps:
        if overlap < o.size:
            overlap = o.size

    d = len(orig) - overlap
    t = len(new) - overlap
    total = d + t

    print "The minimum number of keystrokes to change \"{0}\" to \"{1}\" is {2}".format(orig, new, total)
    print "Need to delete: {}".format(d)
    print "Need to type: {}".format(t)


if __name__ == "__main__":
    # start_time = time.time()
    main()
    # print("\n%s seconds" % (time.time() - start_time))
