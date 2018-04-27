import os
from PIL import Image


def changeRes(dpath, toh, tow):
    list = os.listdir(dpath)
    for pic in list:
        path = dpath + pic
        im = Image.open(path)
        w, h = im.size

        nw = tow
        nh = int(tow * h / w)
        out = im.resize((nw, nh), Image.ANTIALIAS)
        npic = 'new' + pic
        npath = dpath + npic
        out.save(npath)


if __name__ == '__main__':
    iph = 1136
    ipw = 640
    dir_path = 'C:\\Users\\11018\py25\\0005\\'
    changeRes(dir_path, iph, ipw)
