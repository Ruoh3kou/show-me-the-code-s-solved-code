import re
import os


def count(path):
    f = open(path)
    lines = f.readlines()
    word = []

    for line in lines:
        pat = '[a-zA-Z\']+'
        line = re.findall(pat, line)
        word += line

    set1 = set(word)
    word2 = list(set1)

    dir1 = {}
    for x in word2:
        dir1[x] = 0
    for x in word:
        if x in dir1:
            dir1[x] += 1

    print(dir1)


if __name__ == '__main__':
    path = ('0004.txt')
    count(path)
