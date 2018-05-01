import xlrd
import xml.dom.minidom as minidom

comments = '数字信息'


def xlsTOlist(path):
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_index(0)
    d = []
    for i in range(sheet.nrows):
        #处理从EXCEL中读取数字自动为FLOAT型的问题
        r = []
        for ind, j in enumerate(sheet.row_values(i)):
            r.append(int(j))
        d.append(r)
    return d

def writeXml(path):
    data = xlsTOlist(path)
    dom=minidom.Document()
    root=dom.createElement('root')
    numbers=dom.createElement('numbers')
    comment=dom.createComment(comments)
    xmlcontent=dom.createTextNode(str(data))

    dom.appendChild(root)
    root.appendChild(numbers)
    numbers.appendChild(comment)
    numbers.appendChild(xmlcontent)

    with open('numbers.xml','wb') as f:
        f.write(dom.toprettyxml(encoding='utf-8'))

if __name__ == '__main__':
    path='numbers.xls'
    writeXml(path)
