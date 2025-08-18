# Yandex / Хендбуки / Основы Python
# 5.1. Объектная модель Python. Классы, поля и методы


def p_5_1_a():
    """
    Объектно-ориентированное программирование — популярная парадигма
    в современном мире. Это вполне очевидно, ведь любой объект реального
    мира мы теперь можем представить в виде цифрового набора полей и
    методов. Давайте приступим к проектированию классов.
    Разработайте класс Point, который при инициализации принимает
    координаты точки на декартовой плоскости и сохраняет их в
    поля x и y соответственно.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # point = Point(3, 5)
        # print(point.x, point.y) # 3 5


def p_5_1_b():
    """
    Давайте расширим функционал класса, написанного в прошлой задаче.
    Реализуйте методы:
    - move, который перемещает точку на заданное расстояние
      по осям x и y;
    - length, который определяет до переданной точки расстояние,
      округлённое до сотых.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self, x, y):
            self.x += x
            self.y += y

        def length(self, point):
            point_to_point = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
            return round(point_to_point, 2)

    """
    point = Point(3, 5)
    print((point.x, point.y) == (3, 5))
    point.move(2, -3)
    print((point.x, point.y) == (5, 2))

    first_point = Point(2, -7)
    second_point = Point(7, 9)
    print(first_point.length(second_point) == 16.76)
    print(second_point.length(first_point) == 16.76)
    """


def p_5_1_с():
    """
    Если написать предупреждение «Не нажимай красную кнопку!»,
    то её сразу безумно хочется нажать.
    Напишите класс RedButton, который описывает красную кнопку.
    Класс должен реализовывать методы:
    - click() — эмулирует нажатие кнопки, выводит сообщение "Тревога!";
    - count() — возвращает количество раз, которое была нажата кнопка.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class RedButton:

        def __init__(self) -> None:
            self.counter = 0

        def click(self):
            self.counter += 1
            print("Тревога!")

        def count(self):
            return self.counter

    """
    first_button = RedButton()
    second_button = RedButton()
    for time in range(5):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()
    print((first_button.count(), second_button.count()) == (2, 3))
    """


def p_5_1_d():
    """
    Рассмотрим объект «Программист», который задаётся именем,
    должностью и количеством отработанных часов. Каждая должность
    имеет собственный оклад (заработную плату за час работы).
    В нашей импровизированной компании существуют 3 должности:
    - Junior — с окладом 10 тугриков в час;
    - Middle — с окладом 15 тугриков в час;
    - Senior — с окладом 20 тугриков в час по умолчанию и +1
      тугрик за каждое новое повышение.
    Напишите класс Programmer, который инициализируется именем
    и должностью (отработка у нового работника равна нулю).
    Класс реализует следующие методы:
    - work(time) — отмечает новую отработку в количестве часов time;
    - rise() — повышает программиста;
    - info() — возвращает строку для бухгалтерии в формате:
    <имя> <количество отработанных часов>ч. <накопленная зарплата>тгр.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """
    # Сплошное TDD: задание можно не читать - читайте тесты

    class Programmer:
        _grades = {"Junior": 10, "Middle": 15, "Senior": 20}

        def __init__(self, name, grade) -> None:
            self.name = name
            self.grade = grade
            self.hours = 0
            self.salary = 0
            self.worked = 0
            self.rate = self._grades[grade]

        def work(self, time):
            self.hours += time

        def rise(self):
            self.worked += self.hours
            self.salary += self.hours * self.rate
            self.hours = 0
            if self.grade == "Junior":
                self.grade = "Middle"
                self.rate = self._grades[self.grade]
            elif self.grade == "Middle":
                self.grade = "Senior"
                self.rate = self._grades[self.grade]
            else:
                self.rate += 1

        def info(self):
            time = self.hours + self.worked
            salary = self.hours * self.rate + self.salary
            return f"{self.name} {time}ч. {salary}тгр."

    """
    programmer = Programmer("Васильев Иван", "Junior")
    programmer.work(750)
    print(programmer.info() == "Васильев Иван 750ч. 7500тгр.")
    programmer.rise()
    programmer.work(500)
    print(programmer.info() == "Васильев Иван 1250ч. 15000тгр.")
    programmer.rise()
    programmer.work(250)
    print(programmer.info() == "Васильев Иван 1500ч. 20000тгр.")
    programmer.rise()
    programmer.work(250)
    print(programmer.info() == "Васильев Иван 1750ч. 25250тгр.")
    """


def p_5_1_e():
    """
    Давайте перейдём к более сложным геометрическим фигурам.
    Разработайте класс Rectangle.
    При инициализации класс принимает два кортежа рациональных
    координат противоположных углов прямоугольника
    (со сторонами параллельными осям координат).
    Класс должен реализовывать методы:
    - perimeter — возвращает периметр прямоугольника;
    - area — возвращает площадь прямоугольника.
    Все результаты вычислений нужно округлить до сотых.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Rectangle:

        def __init__(self, point1, point2) -> None:
            x1, y1 = point1
            x2, y2 = point2
            self.x = round(min(x1, x2), 2)
            self.y = round(max(y1, y2), 2)
            self.width = round(abs(x1 - x2), 2)
            self.height = round(abs(y1 - y2), 2)

        def perimeter(self):
            return round((self.width + self.height) * 2, 2)

        def area(self):
            return round(self.width * self.height, 2)

    # rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    # print(rect.perimeter() == 23.52)
    # rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    # print(rect.area() == 32.14)


def p_5_1_f():
    """
    Расширим функционал класса написанного вами в предыдущей задаче.
    Реализуйте методы:
    - get_pos() — возвращает координаты верхнего левого угла в виде кортежа;
    - get_size() — возвращает размеры в виде кортежа;
    - move(dx, dy) — изменяет положение на заданные значения;
    - resize(width, height) — изменяет размер
      (положение верхнего левого угла остаётся неизменным).
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Rectangle:

        def __init__(self, point1, point2) -> None:
            x1, y1 = point1
            x2, y2 = point2
            self.x = round(min(x1, x2), 2)
            self.y = round(max(y1, y2), 2)
            self.width = round(abs(x1 - x2), 2)
            self.height = round(abs(y1 - y2), 2)

        def perimeter(self):
            return round((self.width + self.height) * 2, 2)

        def area(self):
            return round(self.width * self.height, 2)

        def get_pos(self):
            return self.x, self.y

        def get_size(self):
            return self.width, self.height

        def move(self, dx, dy):
            self.x = round(self.x + dx, 2)
            self.y = round(self.y + dy, 2)

        def resize(self, width, height):
            self.width = width
            self.height = height

    """
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.get_pos() == (3.2, 3.14), rect.get_size() == (4.32, 7.44))
    rect.move(1.32, -5)
    print(rect.get_pos() == (4.52, -1.86), rect.get_size() == (4.32, 7.44))
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos() == (3.2, 3.14), rect.get_size() == (4.32, 7.44))
    rect.resize(23.5, 11.3)
    print(rect.get_pos() == (3.2, 3.14), rect.get_size() == (23.5, 11.3))

    """


def p_5_1_g():
    """
    Необходимо ещё немного доработать предыдущую задачу.
    Разработайте методы:
    - turn() — поворачивает прямоугольник на 90° по часовой
      стрелке вокруг его центра;
    - scale(factor) — изменяет размер в указанное количество
      раз, тоже относительно центра.
    Все вычисления производить с округлением до сотых.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Rectangle:

        def __init__(self, point1, point2) -> None:
            x1, y1 = point1
            x2, y2 = point2
            self.x = round(min(x1, x2), 2)
            self.y = round(max(y1, y2), 2)
            self.width = round(abs(x1 - x2), 2)
            self.height = round(abs(y1 - y2), 2)

        def perimeter(self):
            return round((self.width + self.height) * 2, 2)

        def area(self):
            return round(self.width * self.height, 2)

        def get_pos(self):
            return self.x, self.y

        def get_size(self):
            return self.width, self.height

        def move(self, dx, dy):
            self.x = round(self.x + dx, 2)
            self.y = round(self.y + dy, 2)

        def resize(self, width, height):
            self.width = width
            self.height = height

        def turn(self):
            mid_x, mid_y = self.x + self.width / 2, self.y - self.height / 2
            self.width, self.height = self.height, self.width
            self.x, self.y = round(mid_x - self.width / 2, 2), round(
                mid_y + self.height / 2, 2
            )

        def scale(self, factor):
            mid_x, mid_y = self.x + self.width / 2, self.y - self.height / 2
            self.width, self.height = round(self.width * factor, 2), round(
                self.height * factor, 2
            )
            self.x, self.y = round(mid_x - self.width / 2, 2), round(
                mid_y + self.height / 2, 2
            )

    """
    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    print(rect.get_pos() == (-3.14, 2.71), rect.get_size() == (6.28, 5.42))
    rect.turn()
    print(rect.get_pos() == (-2.71, 3.14), rect.get_size() == (5.42, 6.28))

    rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
    # print(rect.get_pos() == (-3.14, 2.71), rect.get_size() == (6.28, 5.42))
    rect.scale(2.0)
    print(rect.get_pos() == (-6.28, 5.42), rect.get_size() == (12.56, 10.84))
    """


def p_5_1_h():
    """
    Шашки очень занимательная игра, которую достаточно легко
    моделировать. Правила подразумевают наличие двух классов:
    игральная доска и шашка. Однако мы немного упростим себе
    задачу и вместо шашки будем манипулировать клетками, которые
    могут находиться в трех состояниях: пустая, белая шашка
    и чёрная шашка.
    Разработайте два класса: Checkers и Cell.
    Объекты класса Checkers при инициализации строят игральную
    доску со стандартным распределением клеток и должны
    обладать методами:
    - move(f, t) — перемещает шашку из позиции f в позицию t;
    - get_cell(p) — возвращает объект «клетка» в позиции p.
    Объекты класса Cell при инициализации принимают одно из
    трех состояний:
     W — белая шашка, B — чёрная шашка, * — пустая клетка,
     а также обладают методом status() возвращающим заложенное
     в ней состояние.

    Координаты клеток описываются строками вида PQ, где:
    P — столбец игральной доски, одна из заглавных
    латинских букв: ABCDEFGH;
    Q — строка игральной доски, одна из цифр: 12345678.
    Будем считать, что пользователь всегда ходит правильно
    и контролировать возможность хода не требуется.

    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """
    # в тексте задачи пустая ячейка отмечена как "*",
    # по тестам же должен быть "X"

    class Checkers:
        def __init__(self) -> None:
            board = {p: {p: Cell() for p in "12345678"} for p in "ABCDEFGH"}
            for col, row in board.items():
                if col in "ACEG":
                    row["1"], row["3"], row["7"] = Cell("W"), Cell("W"), Cell("B")
                else:
                    row["2"], row["6"], row["8"] = Cell("W"), Cell("B"), Cell("B")
            self.board = board

        def show(self):
            # for tests
            print(
                "\n",
                *(
                    " ".join(self.get_cell(col + row).status() for col in "ABCDEFGH")
                    for row in "87654321"
                ),
                sep="\n",
                end="\n",
            )

        def move(self, f, t):
            cell = self.get_cell(f)
            self.board[t[0]][t[1]] = cell
            self.board[f[0]][f[1]] = Cell("X")

        def get_cell(self, p):
            return self.board[p[0]][p[1]]

    class Cell:
        def __init__(self, state="X") -> None:
            if state in "WBX":
                self.state = state

        def status(self):
            return self.state

    """
    checkers = Checkers()
    checkers.show()

    checkers = Checkers()
    checkers.move("C3", "D4")
    checkers.move("H6", "G5")
    checkers.show()
        """


def p_5_1_i():
    """
    В программировании существует потребность не только в изученных
    нами коллекциях. Одна из таких очередь. Она реализует подход к
    хранению данных по принципу «Первый вошёл – первый ушел».
    Реализуйте класс Queue, который не имеет параметров
    инициализации, но поддерживает методы:
    - push(item) — добавить элемент в конец очереди;
    - pop() — «вытащить» первый элемент из очереди;
    - is_empty() — проверят очередь на пустоту.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Queue:
        def __init__(self):
            self.queue = []

        def push(self, item):
            self.queue.append(item)

        def pop(self):
            return self.queue.pop(0)

        def is_empty(self):
            return len(self.queue) == 0

    """
    queue = Queue()
    for item in range(10):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop(), end=" ")
    print("\n0 1 2 3 4 5 6 7 8 9")

    queue = Queue()
    for item in ("Hello,", "world!"):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop())
    print("Hello,\nworld!")
    """


def p_5_1_j():
    """
    Ещё одной полезной коллекцией является стек реализующий
    принцип «Последний пришёл – первый ушёл». Его часто представляют
    как стопку карт или магазин пистолета, где приходящие элементы
    закрывают выход уже находящимся в коллекции.
    Реализуйте класс Stack, который не имеет параметров
    инициализации, но поддерживает методы:
    - push(item) — добавить элемент в конец стека;
    - pop() — «вытащить» первый элемент из стека;
    - is_empty() — проверяет стек на пустоту.
    Примечание Ваше решение должно содержать только классы и функции.
    В решении не должно быть вызовов инициализации требуемых классов.
    """

    class Stack:
        def __init__(self) -> None:
            self.stack = []

        def push(self, item):
            self.stack.append(item)

        def pop(self):
            return self.stack.pop()

        def is_empty(self):
            return len(self.stack) == 0

    """
    stack = Stack()
    for item in range(10):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print("\n9 8 7 6 5 4 3 2 1 0")

    stack = Stack()
    for item in ("Hello,", "world!"):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())
    print("world!\nHello,")
    """
