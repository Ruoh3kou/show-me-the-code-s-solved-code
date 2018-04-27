import re


def count():
    f = open('0004.txt')
    lines = f.readlines()
    word = []

    for line in lines:
        line = line.replace(',', ' ')
        line = line.replace('.', '')
        list1 = line.split()
        word += list1

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
    count()
