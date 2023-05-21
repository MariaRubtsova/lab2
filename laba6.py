def zad1():
    strana = {'Россия': 'Москва', 'Казахстан': 'Астана', 'США': 'Вашингтон', 'Канада': 'Оттава'}
    sp_strana = list(strana.keys())
    sp_strana.sort()
    for i in sp_strana:
        print(i, ':', strana[i])
    print(strana, strana['Россия'])


def zad2():
    d = {'АВЕИНОРСТ': 1, 'ДКЛМПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}

    def fun(x):
        for key in d:
            if x in key:
                return d.get(key)

    print(sum(map(fun, input())))

def zad3():
    import random

    students = {"Иванов", "Петров", "Смирнов", "Сидоров", "Васильев", "Кузнецов", "Попов", "Федоров", "Лебедев",
                "Семенов"}
    languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}

    lang_stud = {}

    for st in students:
        kolvo = random.randint(1, 3)
        lang_stud[st] = random.sample(list(languages), kolvo)

    unique_lang = set()
    for i in lang_stud:
        unique_lang = unique_lang.union(set(lang_stud[i]))

    print("Множество различных языков, которые знают студенты: ", sorted(unique_lang), f" ({len(unique_lang)})")

    china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
    print("Студенты, знающие китайский: ", china)

zad3()