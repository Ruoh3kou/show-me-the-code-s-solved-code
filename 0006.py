import os
import re
from collections import Counter
# 读取文件夹下每一个日记
# 选取每一篇中频率最高的三个单词作为重要单词


def pickKeyWord(path):
    diarys = os.listdir(path)
    stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that',
                 'this', 's', 'is', 'are', 'a', 'with', 'as', 'an']
    keyWords = []
    for d in diarys:
        f = open(path + d)
        lines = f.readlines()
        word = []

        for line in lines:
            pat = '[a-zA-Z\']+'
            line = re.findall(pat, line)
            word += line

        wordCounter = Counter(word)
        for i in stop_word:
            wordCounter[i] = 0
        keyWord = wordCounter.most_common()[:2]
        keyWords += keyWord

    print(keyWords)


if __name__ == '__main__':
    path = "0006//"
    pickKeyWord(path)
