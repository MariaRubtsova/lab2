from PIL import Image
def zad1():
    image = Image.open('1.jpg')
    with Image.open('1.jpg') as img:
        img.load()
    image.show()

    width, height = img.size
    print('Ширина', width)
    print('высотоа', height)
    print('формат', img.format)
    print('цветовая модель', img.mode)

def zad2():
    image = '1.jpg'
    with Image.open(image) as img:
        img.load()

    new_image = img.resize((img.width // 3, img.height // 3))
    new_image.save('1_malenkiy.jpg')

    zerv_image = img.transpose(Image.FLIP_TOP_BOTTOM)
    zerv_image.save('zerv_1.jpg')
    zerv_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    zerv_image.save('zerv1_1.jpg')

def zad3():
    import os
    imags = os.listdir('pic')
    for image in imags:
        with Image.open(image) as img:
            img.load()
            new_img = img.convert("L")
            new_img.save(f'pic/{image}.jpg')


def zad4():
    im1 = Image.open('1.jpg')
    im2 = Image.open('2.jpg')
    im1.paste(im2)
    im1.save('fon_pillow_paste.jpg')




zad4()