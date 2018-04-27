import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter


def randomColor():
    return (random.randint(32, 127), random.randint(
        32, 127), random.randint(32, 127))


def randomColor2():
    return (random.randint(60, 255), random.randint(
        60, 255), random.randint(60, 255))


def randomText():
    return random.sample(string.ascii_letters, 4)


def createIdenCode():
    width = 60 * 4
    height = 60
    img = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('c:\\windows\\fonts\\Arial.ttf', 45)
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randomColor())
    for x, y in enumerate(randomText()):
        draw.text((60 * x + 10, 10), y,
                  font=font, fill=randomColor2())
    img = img.filter(ImageFilter.BLUR)

    img.show()


if __name__ == '__main__':
    createIdenCode()
