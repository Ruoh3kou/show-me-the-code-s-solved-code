from PIL import Image, ImageDraw, ImageFont, ImageColor


def addNum(img):
    draw = ImageDraw.Draw(img)  # 新建draw对象
    font = ImageFont.truetype(
        'c:\\windows\\fonts\\Arial.ttf', size=50)  # 新建字体对象
    color = ImageColor.colormap.get('red')
    w, h = img.size  # 原图宽、长
    draw.text((w - 50, 0), '4', font=font, fill=color)
    img.save('0000(2).jpg')


if __name__ == '__main__':
    im = Image.open('0000.jpg')
    addNum(im)
