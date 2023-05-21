def zad1():
    numbers = [1, 2, 5, 6, 9]
    x = int(input('угадайте число: '))
    if x in numbers:
        print('вы угадали!')
    else:
        print('нет такого числа!')


def zad2():
    sp = list(map(int, input().split()))
    for i in range(len(sp)):
        if sp.count(i) > 1:
            print(i)


def zad3():
    sp = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
    x = int(input('сколько хотите выходных?: '))
    x = len(sp) - x
    print('рабочие дни: ', *sp[0:x])
    print('выходные дни: ', *sp[x:len(sp) + 1])


def zad4():
    import random
    a = ['Коровашев', 'Рябков', 'Ольховский']
    b = ['Иванов', 'Петров', 'Васечкин']
    a1 = random.sample(a, 2)
    b1 = random.sample(b, 2)
    comanda = tuple(a1) + tuple(b1)
    if 'Иванов' in comanda:
        print('YES', comanda.count('Иванов'))
    else:
        print('NO')
    print(a, b, comanda, len(comanda))

zad4()

