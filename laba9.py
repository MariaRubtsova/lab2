from PIL import Image
def zad2():
    import os
    imags = os.listdir('pic')
    for image in imags:
        with Image.open(image) as img:
            img.load()
            new_img = img.convert("L")
            new_img.save(f'pic/{image}.jpg')

def zad3():
    import csv
    file = open('data.csv', 'r')
    data = list(csv.reader(file, delimiter=','))
    print("Нужно купить:")
    for i in data:
        print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
    print(f"итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")

zad3()