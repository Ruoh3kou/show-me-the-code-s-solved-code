import os
import re


def statcCode(path):
    totalLines = 0
    commentLines = 0
    blankLines = 0
    codeLines = 0
    files = os.listdir(path)
    for x in files:
        if re.match('.*\.py', x) is not None:
            f = open(x, 'r', encoding='UTF-8')
            lines = f.readlines()
            totalLines += len(lines)
            for line in lines:
                if re.match('#.*', line)is not None:
                    commentLines += 1
                elif re.match('^$', line)is not None:
                    blankLines += 1
                else:
                    codeLines += 1
    print("总行数为：%d" % totalLines)
    print("空白行为：%d" % blankLines)
    print("注释行为：%d" % commentLines)
    print("代码行为：%d" % codeLines)


if __name__ == '__main__':
    path = 'C:\\Users\\11018\\projects\\py25\\'
    statcCode(path)
