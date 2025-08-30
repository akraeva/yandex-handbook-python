# Yandex / Хендбуки / Основы Python
# 6.2. Модуль pandas

from numpy import arange
import re
import pandas as pd


def p_6_2_a():
    """
    Напишите функцию length_stats, которая получает текст,
    а возвращает объект Series со словами в качестве индексов
    и их длинами в качестве значений.
    Все слова в тексте предварительно переведите в нижний регистр,
    избавьтесь от знаков препинания и цифр, а также отсортируйте
    в лексикографическом порядке.
    """

    # import re
    # import pandas as pd

    def length_stats(text):
        pattern = r"[a-zа-яё]+"
        words = sorted(set(re.findall(pattern, text.lower())))
        return pd.Series({word: len(word) for word in words})

    # print(length_stats("Мама мыла раму"))
    # print(length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка."))


def p_6_2_b():
    """
    В этот раз продумайте функцию length_stats, которая получает текст,
    а возвращает пару объектов Series со словами в качестве индексов
    и их длинами в качестве значений.
    Все слова в тексте предварительно переведите в нижний регистр,
    избавьтесь от знаков препинания и цифр, а также отсортируйте в
    лексикографическом порядке.
    """

    # import re
    # import pandas as pd

    def length_stats(text):
        pattern = r"[a-zа-яё]+"
        words = sorted(set(re.findall(pattern, text.lower())))
        odd = pd.Series(
            {word: len(word) for word in words if len(word) % 2 != 0}, dtype=int
        )
        even = pd.Series(
            {word: len(word) for word in words if len(word) % 2 == 0}, dtype=int
        )
        return odd, even

    """
    odd, even = length_stats("Мама мыла раму")
    print(odd)
    print(even)
    odd, even = length_stats("Лес, опушка, странный домик. Лес, опушка и зверушка.")
    print(odd)
    print(even)
    """


def p_6_2_с():
    """
    В местном магазине решили добавить анализ данных и
    каждый чек представлять в виде DataFrame.
    Прайс-лист уже сформирован в виде объекта Series,
    где индексами являются названия, а значениями — цены.

    Напишите функцию, cheque, которая принимает прайс-лист
    и список покупок в виде неопределённого количества
    именованных параметров (ключ — название товара, значение — количество)

    Функция должна вернуть объект DataFrame со столбцами:
    - наименование продукта (product);
    - цена за единицу (price);
    - количество (number);
    = итоговая цена (cost).
    Строки чека должны быть отсортированы по названию
    продуктов в лексикографическом порядке.
    """

    # import pandas as pd

    def cheque(prices, **kwargs):

        df = pd.DataFrame(
            {
                "product": list(kwargs.keys()),
                "price": [prices[product] for product in kwargs.keys()],
                "number": list(kwargs.values()),
            }
        )
        df["cost"] = df["price"] * df["number"]
        return df.sort_values("product").reset_index(drop=True)

    """
    products = ["bread", "milk", "soda", "cream"]
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    print(result)
    """
    """
    product  price  number  cost
    0   cream     72       1    72
    1    milk     58       2   116
    2    soda     99       3   297
    """


def p_6_2_d():
    """
    Магазин, для которого вы писали функцию в предыдущей
    задаче, проводит акцию:
    При покупке больше двух товаров — скидка 50%
    мелкий шрифт: скидка распространяется только на
    товары купленные в количестве более двух штук
    Напишите функцию discount, принимающую чек из прошлой
    задачи и возвращающую новый с учётом акции.
    Примечание Не удаляйте функцию cheque, она потребуется
    для тестирования.
    """

    # import pandas as pd

    def cheque(prices, **kwargs):

        df = pd.DataFrame(
            {
                "product": list(kwargs.keys()),
                "price": [prices[product] for product in kwargs.keys()],
                "number": list(kwargs.values()),
            }
        )
        df["cost"] = df["price"] * df["number"]
        return df.sort_values("product").reset_index(drop=True)

    def discount(default_cheque):
        dc = default_cheque.copy()
        dc.loc[dc["number"] > 2, "cost"] = dc.loc[dc["number"] > 2, "cost"] * 0.5
        return dc

    """
    products = ["bread", "milk", "soda", "cream"]
    prices = [37, 58, 99, 72]
    price_list = pd.Series(prices, products)
    result = cheque(price_list, soda=3, milk=2, cream=1)
    with_discount = discount(result)
    print(result)
    print(with_discount)
    """
    """
    product  price  number  cost
    0   cream     72       1    72
    1    milk     58       2   116
    2    soda     99       3   297
    product  price  number   cost
    0   cream     72       1   72.0
    1    milk     58       2  116.0
    2    soda     99       3  148.5
    """


def p_6_2_e():
    """
    Фильтрация данных — одна из первостепенных задач их анализа.
    Напишите функцию get_long, принимающую серию формата первой
    задачи и фильтрующую её по именованному параметру min_length
    (по умолчанию 5).
    """

    # import pandas as pd

    def get_long(words, min_length=5):
        return words[words >= min_length]

    """
    data = pd.Series([3, 5, 6, 6], ["мир", "питон", "привет", "яндекс"])
    filtered = get_long(data)
    print(data)
    print(filtered)

    data = pd.Series([3, 5, 6, 6], ["мир", "питон", "привет", "яндекс"])
    filtered = get_long(data, min_length=6)
    print(data)
    print(filtered)
    """


def p_6_2_f():
    """
    Во всех без исключения учебных заведениях ведутся журналы
    успеваемости. Это отличный пример данных, подлежащих обработке.
    Рассмотрим журнал летней олимпиадной школы, в которой основными
    предметами выступают математика, физика и информатика.
    Данные об успеваемости представлены DataFrame со столбцами:
    - name — имя;
    - maths — оценка по математике;
    - physics — оценка по физике;
    - computer science — оценка по информатике.
    Напишите функцию best, которая фильтрует всех «ударников» в журнале.
    """

    # import pandas as pd

    def best(students):
        subjects = students[["maths", "physics", "computer science"]]
        return students[subjects.gt(3).all(axis=1)]

    """
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = best(journal)
    print(journal)
    print(filtered)
    """


def p_6_2_g():
    """
    Продолжим обрабатывать DataFrame из прошлой задачи.
    Напишите функцию need_to_work_better, которая выбирает
    тех, у кого есть хотя бы одна двойка.
    """

    # import pandas as pd

    def need_to_work_better(students):
        subjects = students[["maths", "physics", "computer science"]]
        return students[subjects.eq(2).any(axis=1)]

    """
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = need_to_work_better(journal)
    print(journal)
    print(filtered)
    """


def p_6_2_h():
    """
    Продолжим обрабатывать DataFrame из прошлых задач.
    Напишите функцию update, которая добавляет к данным столбец
    average, содержащий среднюю оценку ученика, а также сортирует
    данные по убыванию этого столбца, а при равенстве средних —
    по имени лексикографически.
    """

    # import pandas as pd

    def update(students):
        subjects = students[["maths", "physics", "computer science"]]
        st = students.copy()
        st["average"] = subjects.mean(axis=1)
        return st.sort_values(by=["average", "name"], ascending=[False, True])

    """
    columns = ["name", "maths", "physics", "computer science"]
    data = {
        "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
        "maths": [5, 4, 5, 2, 4],
        "physics": [4, 4, 4, 5, 5],
        "computer science": [5, 2, 5, 4, 3],
    }
    journal = pd.DataFrame(data, columns=columns)
    filtered = update(journal)
    print(journal)
    print(filtered)
    """


def p_6_2_i():
    """
    Представьте себе поле морского боя, которое не имеет границ.
    Для простоты координаты выстрелов будем обозначать целыми
    координатами на плоскости.
    Бесконечное поле порождает большое количество данных, которые
    требуется проанализировать. Один из игроков для упрощения этой
    задачи просит вас написать программу, которая обрезает данные
    до ограниченного прямоугольника.

    Формат ввода В первой строке записано два числа — координаты
    верхнего левого угла. Во второй строке — правого нижнего.
    В файле data.csv находится датасет с координатами всех
    выстрелов противника.
    Формат вывода Часть датасета, ограниченная заданным прямоугольником.
    """

    # import pandas as pd

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    file_name = "data.csv"  # for tests "data_6_2/data.csv"
    data = pd.read_csv(file_name)
    print(data.loc[data["x"].between(x1, x2) & data["y"].between(y2, y1)])

    """
    >> 10 0
    >> 0 10

            x   y
    6262     9   0
    59060   10   4
    69882   10   5
    72739    0   0
    120951   3   1
    137931   9  10
    183595   7   0
    194157   0   9
    219910   0   3
    220920  10   0
    242318   8   4
    283651   1   8
    292990   4   3
    294474   6   3
    352959  10  10
    393223   3   5
    423449   1   2
    """


def p_6_2_j():
    """
    Экстремум в математике — максимальное или минимальное значение
    функции на заданном множестве.
    Чаще всего математики для поиска экстремума функции прибегают
    к её дифференцированию. Однако мы можем обойти этот трудоёмкий
    процесс и схитрить.
    Напишите три функции:
    - values(func, start, end, step), строящую Series значений
      функции в точках диапазона и принимающую:
    - функцию одной переменной;
    - начало диапазона;
    - конец диапазона;
    - шаг вычисления;
    - min_extremum(data) возвращает точку, в которой был достигнут
      минимум на диапазоне;
    - max_extremum(data) возвращает точку, в который был достигнут
      максимум на диапазоне.
    """

    # from numpy import arange
    # import pandas as pd

    def values(func, start, end, step):
        args = [x for x in arange(start, end + step, step)]
        return pd.Series([func(x) for x in args], index=args)

    def min_extremum(data):
        return data.idxmin()

    def max_extremum(data):
        return data.idxmax()

    """
    data = values(lambda x: x**2 + 2 * x + 1, -1.5, 1.7, 0.1)
    print(data)
    print(min_extremum(data))
    print(max_extremum(data))
    """
    """
    -1.500000e+00    0.25
    -1.400000e+00    0.16
    ...
    1.700000e+00    7.29
    dtype: float64
    -0.9999999999999996
    1.7000000000000028
    """
