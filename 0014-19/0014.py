import xlwt
import json
import codecs

def writeExcel(path):
    f = codecs.open(path,encoding='utf-8')
    data = json.loads(f.read())
    wbk=xlwt.Workbook()
    table=wbk.add_sheet('test')
    for row,i in enumerate(data):
        table.write(row,0,i)
        for col,j in enumerate(data[i]):
            table.write(row, col+1, j)
    wbk.save(path[:-4]+'.xls')

if __name__ == '__main__':
    path="student.txt"
    writeExcel(path)