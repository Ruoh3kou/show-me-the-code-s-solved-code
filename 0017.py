import xlrd
import xml.dom.minidom as minidom

comments = '学生信息表\n"id" : [名字, 数学, 语文, 英文]'
def xlsTOset(path):
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_index(0)
    d = {}
    for i in range(sheet.nrows):
        d[i+1]=sheet.row_values(i)[1:]
    return d

def writeXml(path):
    data=xlsTOset(path)
    dom=minidom.Document()
    root=dom.createElement('root')
    students=dom.createElement('students')
    comment=dom.createComment(comments)
    xmlcontent=dom.createTextNode(str(data))

    dom.appendChild(root)
    root.appendChild(students)
    students.appendChild(comment)
    students.appendChild(xmlcontent)

    with open('students.xml','wb') as f:
        f.write(dom.toprettyxml(encoding='utf-8'))

if __name__ == '__main__':
    path='student.xls'
    writeXml(path)
