import xlwt
import json
import codecs


def writeExcel(path):
    f = codecs.open(path, encoding='utf-8')
    data = json.loads(f.read())
    wbk = xlwt.Workbook()
    table = wbk.add_sheet('test')
    for row, i in enumerate(data):
        for col,j in enumerate(i):
            table.write(row,col,j)
    wbk.save(path[:-4]+'.xls')


if __name__ == '__main__':
    path = "numbers.txt"
    writeExcel(path)
