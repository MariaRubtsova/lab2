from PIL import Image, ImageFont, ImageDraw
def zad1():
    image = Image.open('dr.jpg')
    with Image.open('dr.jpg') as img:
        img.load()
    image.show()
    cropped_img = img.crop((10, 100, 480, 400))
    cropped_img.show()
    cropped_img.save('cropped_dr.jpg')

def zad2():
    holiday_cards = {'8 марта': '8mart.jpg',
                     'День Победы': '9may.jpg',
                     'День Рождения': 'dr.jpeg'
                     }
    x = input('Введите праздник: ')
    for key in holiday_cards:
        if key == x:
            y = Image.open(holiday_cards[key])
            y.show()

def zad3():
    image = Image.open('dr.jpg')
    with Image.open('dr.jpg') as img:
        img.load()
    #image.show()

    cropped_img = img.crop((10, 180, 480, 500))

    x = input('Кого хотите поздравить?: ')

    font = ImageFont.truetype('arial.ttf', size=18)
    image = ImageDraw.Draw(cropped_img)
    image.text((10, 10), x, font = font)


    cropped_img.show()

    #cropped_img.save('cropped_dr.jpg')


zad3()