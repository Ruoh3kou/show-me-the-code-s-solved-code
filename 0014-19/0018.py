import xlrd
import xml.dom.minidom as minidom
comments = '城市信息\n'


def xlsTOset(path):
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_index(0)
    d = {}
    for i in range(sheet.nrows):
        d[i+1] = sheet.row_values(i)[1:]
    return d


def writeXml(path):
    data = xlsTOset(path)
    dom = minidom.Document()
    root = dom.createElement('root')
    cities = dom.createElement('cities')
    comment = dom.createComment(comments)
    xmlcontent = dom.createTextNode(str(data))

    dom.appendChild(root)
    root.appendChild(cities)
    cities.appendChild(comment)
    cities.appendChild(xmlcontent)

    with open('city.xml', 'wb') as f:
        f.write(dom.toprettyxml(encoding='utf-8'))


if __name__ == '__main__':
    path = 'city.xls'
    writeXml(path)
