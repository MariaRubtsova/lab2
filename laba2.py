def zad1():
    a = int(input("введите номер места "))
    if a % 2 == 0 and a <= 36:
        print('Вверхнее место в купе')
    elif a % 2 != 0 and a <= 35:
        print('Нижннее место в купе')
    elif a % 2 == 0 and a > 36:
        print('Вверхнее боковое место')
    else:
        print('Нижнее боковое место')


def sad2():
    password = input('Введите пароль: ')

    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False

    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "@#%&":
            is_spec = True

    if len(password) > 4 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль: Oк')
    else:
        print('Пароль слишком простой')
    proc2(), proc1()


def zad3():
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(' ДАТ весокосный')
    else:
        print('НЕТЪ не весокосный')

def zad4():
    ne_color, two_color = input('Первый цвет: '), input('Второй цвет: ')
    colors = ['красный', 'синий', 'желтый', 'фиолетовый', 'оранжевый', 'зеленый']
    res_color = 'Не верно введены цвета'
    if one_color in colors[:3] and two_color in colors[:3]:
        res_color = one_color if one_color == two_color else colors[
            colors.index(one_color) + colors.index(two_color) + 2]
    print(res_color)





