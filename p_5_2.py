# Yandex / Хендбуки / Основы Python
# 5.2. Волшебные методы, переопределение методов. Наследование


def p_5_2_a():
    """
    Давайте расширим функционал класса, написанного вами в задаче
    «Классная точка 2.0» (предыдущий параграф).
    Создайте класс PatchedPoint — наследника уже написанного вами Point.
    Требуется реализовать следующие виды инициализации нового класса:
    — параметров не передано — координаты точки равны 0;
    — передан один параметр — кортеж с координатами точки;
    — передано два параметра — координаты точки.
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

    # решение
    class PatchedPoint(Point):
        def __init__(self, *args, x=0, y=0):
            if len(args) == 2:
                x, y = args
            elif len(args) == 1 and isinstance(args[0], (tuple, list)):
                x, y = args[0]
            self.x = x
            self.y = y


def p_5_2_b():
    """
    А теперь модернизируем уже новый класс PatchedPoint.
    Реализуйте магические методы _str_ и _repr_.
    При преобразовании в строку точка представляется в формате (x, y).
    Репрезентация же должна возвращать строку для инициализации точки
    двумя параметрами.
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

    class PatchedPoint(Point):
        def __init__(self, *args, x=0, y=0):
            if len(args) == 2:
                x, y = args
            elif len(args) == 1 and isinstance(args[0], (tuple, list)):
                x, y = args[0]
            self.x = x
            self.y = y

        # решение
        def __str__(self) -> str:
            return f"({self.x}, {self.y})"

        def __repr__(self) -> str:
            return f"PatchedPoint({self.x}, {self.y})"


def p_5_2_с():
    """
    Согласитесь, что использовать операторы куда удобнее, чем обыкновенные
    методы. Давайте вспомним о реализованном нами методе move(x, y) и
    напишем ему альтернативу в виде операторов + и +=.
    При выполнении кода point + (x, y), создаётся новая точка, которая
    отличается от изначальной на заданное кортежем расстояние по осям x и y.
    При выполнении кода point += (x, y) производится перемещение
    изначальной точки. Напомним, что сейчас мы модернизируем
    только класс PatchedPoint.
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

    class PatchedPoint(Point):
        def __init__(self, *args, x=0, y=0):
            if len(args) == 2:
                x, y = args
            elif len(args) == 1 and isinstance(args[0], (tuple, list)):
                x, y = args[0]
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return f"({self.x}, {self.y})"

        def __repr__(self) -> str:
            return f"PatchedPoint({self.x}, {self.y})"

        # решение
        def __add__(self, other):
            return PatchedPoint(self.x + other[0], self.y + other[1])

        def __radd__(self, other):
            return self.__add__(other)

        def __iadd__(self, other):
            self.x += other[0]
            self.y += other[1]
            return self


def p_5_2_d():
    """
    Возможно, вы уже заметили, что дробные числа (float) недостаточно
    точные для некоторых задач. Для более точных математических расчётов
    иногда прибегают к созданию правильных рациональных дробей,
    описываемых числителем и знаменателем.
    Начнём разработку класса Fraction, который реализует предлагаемые дроби.
    Предусмотрите возможность инициализации дроби с помощью двух целых
    чисел или строки в формате <числитель>/<знаменатель>.
    В случаях наличия общего делителя у числителя и знаменателя,
    дробь следует сократить. А также реализуйте методы:
    - numerator() — возвращает абсолютное значение числителя;
    - numerator(number) — изменяет значение числителя и производит
      сокращение дроби, если это необходимо;
    - denominator() – возвращает абсолютное значение знаменателя;
    - denominator(number) — изменяет значение знаменателя и производит
      сокращение дроби, если необходимо;
    - __str__ — возвращает строковое представление дроби в формате
      <числитель>/<знаменатель>;
    - __repr__ — возвращает описание объекта в формате
      Fraction(<числитель>, <знаменатель>).
    Примечание Будем считать, что пользователь знает о запрете деления на ноль.
    Все числа в данной задаче будут положительными.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать
    (называть с использованием ведущих символов нижнего подчёркивания).
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1 and isinstance(args[0], str):
                arg = args[0].split("/")
                if len(arg) == 2 and all(a.isdigit() for a in arg):
                    num, den = map(int, arg)
            if num is not None and den is not None:
                self._num = num
                self._den = den
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = self._num, self._den
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = number
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = number
            self._reduce()

        def __str__(self):
            return f"{self._num}/{self._den}"

        def __repr__(self):
            return f"Fraction({self._num}, {self._den})"


def p_5_2_e():
    """
    Продолжим разработку класса Fraction, который реализует
    предлагаемые дроби. Предусмотрите возможность задать отрицательные
    числитель и/или знаменатель. А также перепишите методы
    __str__ и __repr__ таким образом, чтобы информация об объекте
    согласовывалась с инициализацией строкой.
    Далее реализуйте оператор математического отрицания — унарный минус.
    Примечание Будем считать, что пользователь знает о запрете деления на ноль.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать
    (называть с использованием ведущих символов нижнего подчёркивания).
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1 and isinstance(args[0], str):
                arg = args[0].split("/")
                if len(arg) == 2 and all(a.lstrip("-").isdigit() for a in arg):
                    num, den = map(int, arg)
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

    """
    a = Fraction(1, 3)
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)
    print(f"{a} {b} {c} {d}" == "1/3 1/3 -1/3 -1/3")
    print(
        " ".join(map(repr, (a, b, c, d)))
        == "Fraction('1/3') Fraction('1/3') Fraction('-1/3') Fraction('-1/3')"
    )

    a = Fraction("-1/2")
    b = -a
    print(f"{a} {b} {a is b}" == "-1/2 1/2 False")
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(f"{a} {b}" == "1/3 -1/2")
    print(a.numerator() == 1 and a.denominator() == 3)
    print(b.numerator() == 1 and b.denominator() == 2)
    """


def p_5_2_f():
    """
    Продолжим разработку класса Fraction, который реализует
    предлагаемые дроби. Реализуйте бинарные операторы:
    + — сложение дробей, создаёт новую дробь;
    - — вычитание дробей, создаёт новую дробь;
    += — сложение дробей, изменяет дробь, переданную слева;
    -= — вычитание дробей, изменяет дробь, переданную слева.
    Примечание Будем считать, что пользователь знает о запрете деления на ноль.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать
    (называть с использованием ведущих символов нижнего подчёркивания).
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1 and isinstance(args[0], str):
                arg = args[0].split("/")
                if len(arg) == 2 and all(a.lstrip("-").isdigit() for a in arg):
                    num, den = map(int, arg)
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

        # решение
        def __add__(self, other):
            num1 = -self._num if self._neg else self._num
            den1 = self._den
            num2 = -other._num if other._neg else other._num
            den2 = other._den
            res_num = num1 * den2 + num2 * den1
            res_den = den1 * den2
            return Fraction(res_num, res_den)

        def __sub__(self, other):
            return self + (-other)

        def __iadd__(self, other):
            res = self + other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def __isub__(self, other):
            res = self - other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

    """
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    c = a + b
    print(f"{a} {b} {c} {a is c} {b is c}" == "1/3 1/2 5/6 False False")

    a = Fraction(1, 8)
    c = b = Fraction(3, 8)
    b -= a
    print(f"{a} {b} {c} {b is c}" == "1/8 1/4 1/4 True")
    """


def p_5_2_g():
    """
    Продолжим разработку класса Fraction, который реализует
    предлагаемые дроби. Реализуйте бинарные операторы:
    * — умножение дробей, создаёт новую дробь;
    / — деление дробей, создаёт новую дробь;
    *= — умножение дробей, изменяет дробь, переданную слева;
    /= — деление дробей, изменяет дробь, переданную слева.
    Также разработайте метод reverse, возвращающий дробь обратную данной.
     Будем считать, что пользователь знает о запрете деления на ноль.
    Все поля и методы, не требуемые в задаче, следует инкапсулировать
    (называть с использованием ведущих символов нижнего подчёркивания).

    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1 and isinstance(args[0], str):
                arg = args[0].split("/")
                if len(arg) == 2 and all(a.lstrip("-").isdigit() for a in arg):
                    num, den = map(int, arg)
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

        def __add__(self, other):
            num1 = -self._num if self._neg else self._num
            den1 = self._den
            num2 = -other._num if other._neg else other._num
            den2 = other._den
            res_num = num1 * den2 + num2 * den1
            res_den = den1 * den2
            return Fraction(res_num, res_den)

        def __sub__(self, other):
            return self + (-other)

        def __iadd__(self, other):
            res = self + other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def __isub__(self, other):
            res = self - other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        # решение
        def reverse(self):
            return Fraction(-self._den if self._neg else self._den, self._num)

        def __mul__(self, other):
            neg = self._neg != other._neg
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(-num if neg else num, den)

        def __truediv__(self, other):
            return self * other.reverse()

        def __imul__(self, other):
            res = self * other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def __itruediv__(self, other):
            self *= other.reverse()
            return self


def p_5_2_h():
    """
    Следующим этапом разработки будет реализация методов
    сравнения: >, <, >=, <=, ==, !=.
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1 and isinstance(args[0], str):
                arg = args[0].split("/")
                if len(arg) == 2 and all(a.lstrip("-").isdigit() for a in arg):
                    num, den = map(int, arg)
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

        def __add__(self, other):
            num1 = -self._num if self._neg else self._num
            den1 = self._den
            num2 = -other._num if other._neg else other._num
            den2 = other._den
            res_num = num1 * den2 + num2 * den1
            res_den = den1 * den2
            return Fraction(res_num, res_den)

        def __sub__(self, other):
            return self + (-other)

        def __iadd__(self, other):
            res = self + other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def __isub__(self, other):
            res = self - other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def reverse(self):
            return Fraction(-self._den if self._neg else self._den, self._num)

        def __mul__(self, other):
            neg = self._neg != other._neg
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(-num if neg else num, den)

        def __truediv__(self, other):
            return self * other.reverse()

        def __imul__(self, other):
            res = self * other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def __itruediv__(self, other):
            self *= other.reverse()
            return self

        # решение

        def __eq__(self, other):
            # ==
            return (
                self._neg == other._neg
                and self._num == other._num
                and self._den == other._den
            )

        def __ne__(self, other):
            # !=
            return not self == other

        def __gt__(self, other):
            # >
            num1 = -self._num if self._neg else self._num
            num2 = -other._num if other._neg else other._num
            return num1 * other._den > num2 * self._den

        def __lt__(self, other):
            # <
            return self != other and not self > other

        def __ge__(self, other):
            # >=
            return self == other or self > other

        def __le__(self, other):
            # <=
            return not self > other


def p_5_2_i():
    """
    Все же понимают, что целые числа тоже являются дробями?!
    Следовательно, нам требуется изменить систему инициализации,
    чтобы она могла воспринимать и целые числа (причём и в виде
    строк). Ну и естественно, требуется переработать операторы
    арифметических действий и сравнения.
    Будем считать, что пользователь знает о запрете деления на ноль.
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1:
                if isinstance(args[0], int):
                    num = args[0]
                    den = 1
                if isinstance(args[0], str) and args[0]:
                    arg = args[0].split("/")
                    if all(a.lstrip("-").isdigit() for a in arg):
                        if len(arg) == 2:
                            num, den = map(int, arg)
                        elif len(arg) == 1:
                            num = int(arg[0])
                            den = 1
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        # решение в использовании декоратора
        def _convert_to_fraction(method):
            def wrapper(self, other):
                if isinstance(other, int):
                    other = Fraction(other)
                return method(self, other)

            return wrapper

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

        @_convert_to_fraction
        def __add__(self, other):
            num1 = -self._num if self._neg else self._num
            den1 = self._den
            num2 = -other._num if other._neg else other._num
            den2 = other._den
            res_num = num1 * den2 + num2 * den1
            res_den = den1 * den2
            return Fraction(res_num, res_den)

        @_convert_to_fraction
        def __sub__(self, other):
            return self + (-other)

        @_convert_to_fraction
        def __iadd__(self, other):
            res = self + other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        @_convert_to_fraction
        def __isub__(self, other):
            res = self - other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def reverse(self):
            return Fraction(-self._den if self._neg else self._den, self._num)

        @_convert_to_fraction
        def __mul__(self, other):
            neg = self._neg != other._neg
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(-num if neg else num, den)

        @_convert_to_fraction
        def __truediv__(self, other):
            return self * other.reverse()

        @_convert_to_fraction
        def __imul__(self, other):
            res = self * other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        @_convert_to_fraction
        def __itruediv__(self, other):
            self *= other.reverse()
            return self

        @_convert_to_fraction
        def __eq__(self, other):
            # ==
            return (
                self._neg == other._neg
                and self._num == other._num
                and self._den == other._den
            )

        @_convert_to_fraction
        def __ne__(self, other):
            # !=
            return not self == other

        @_convert_to_fraction
        def __gt__(self, other):
            # >
            num1 = -self._num if self._neg else self._num
            num2 = -other._num if other._neg else other._num
            return num1 * other._den > num2 * self._den

        @_convert_to_fraction
        def __lt__(self, other):
            # <
            return self != other and not self > other

        @_convert_to_fraction
        def __ge__(self, other):
            # >=
            return self == other or self > other

        @_convert_to_fraction
        def __le__(self, other):
            # <=
            return not self > other

    """
    a = Fraction(1)
    b = Fraction("2")
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(f"{a} {b} {c} {d}" == "1/1 2/1 1/3 1/1")
    print(f"{a > b} {c > d}" == "False False")
    print(f"{a >= 1} {b >= 1} {c >= 1} {d >= 1}" == "True True False True")

    a = Fraction(1, 2)
    b = Fraction("2/3")
    c, d = map(Fraction.reverse, (a + 2, b - 1))
    print(f"{a} {b} {c} {d}" == "1/2 2/3 2/5 -3/1")
    print(f"{a > b} {c > d}" == "False True")
    print(f"{a >= 1} {b >= 1} {c >= 1} {d >= 1}" == "False False False False")
    """


def p_5_2_j():
    """
    Мы «научили» наши дроби работать с целыми числами и вот
    теперь надо провернуть обратное действие. Реализуйте функционал,
    который позволит производить все арифметические операции
    с дробями и числами, независимо от их положения
    (слева или справа) в операторе.
    """

    class Fraction:

        def __init__(self, *args) -> None:
            num, den = None, None
            if len(args) == 2 and all(isinstance(a, int) for a in args):
                num, den = args
            elif len(args) == 1:
                if isinstance(args[0], int):
                    num = args[0]
                    den = 1
                if isinstance(args[0], str) and args[0]:
                    arg = args[0].split("/")
                    if all(a.lstrip("-").isdigit() for a in arg):
                        if len(arg) == 2:
                            num, den = map(int, arg)
                        elif len(arg) == 1:
                            num = int(arg[0])
                            den = 1
            if num is not None and den is not None:
                self._neg = num * den < 0
                self._num = abs(num)
                self._den = abs(den)
                self._reduce()
            else:
                raise TypeError

        def _reduce(self):
            if self._num == 0:
                self._den = 1
                return
            a, b = abs(self._num), abs(self._den)
            while b:
                a, b = b, a % b
            self._num //= a
            self._den //= a

        def _convert_to_fraction(method):
            def wrapper(self, other):
                if isinstance(other, int):
                    other = Fraction(other)
                return method(self, other)

            return wrapper

        def numerator(self, number=None):
            if number is None:
                return self._num
            self._num = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def denominator(self, number=None):
            if number is None:
                return self._den
            self._den = abs(number)
            self._neg = (number < 0) != self._neg
            self._reduce()

        def __str__(self):
            return f"{"-" if self._neg else ""}{abs(self._num)}/{abs(self._den)}"

        def __repr__(self):
            return f"Fraction('{str(self)}')"

        def __neg__(self):
            return Fraction(self._num if self._neg else -self._num, self._den)

        @_convert_to_fraction
        def __add__(self, other):
            num1 = -self._num if self._neg else self._num
            den1 = self._den
            num2 = -other._num if other._neg else other._num
            den2 = other._den
            res_num = num1 * den2 + num2 * den1
            res_den = den1 * den2
            return Fraction(res_num, res_den)

        @_convert_to_fraction
        def __sub__(self, other):
            return self + (-other)

        @_convert_to_fraction
        def __iadd__(self, other):
            res = self + other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        @_convert_to_fraction
        def __isub__(self, other):
            res = self - other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        def reverse(self):
            return Fraction(-self._den if self._neg else self._den, self._num)

        @_convert_to_fraction
        def __mul__(self, other):
            neg = self._neg != other._neg
            num = self._num * other._num
            den = self._den * other._den
            return Fraction(-num if neg else num, den)

        @_convert_to_fraction
        def __truediv__(self, other):
            return self * other.reverse()

        @_convert_to_fraction
        def __imul__(self, other):
            res = self * other
            self._neg, self._num, self._den = res._neg, res._num, res._den
            return self

        @_convert_to_fraction
        def __itruediv__(self, other):
            self *= other.reverse()
            return self

        @_convert_to_fraction
        def __eq__(self, other):
            # ==
            return (
                self._neg == other._neg
                and self._num == other._num
                and self._den == other._den
            )

        @_convert_to_fraction
        def __ne__(self, other):
            # !=
            return not self == other

        @_convert_to_fraction
        def __gt__(self, other):
            # >
            num1 = -self._num if self._neg else self._num
            num2 = -other._num if other._neg else other._num
            return num1 * other._den > num2 * self._den

        @_convert_to_fraction
        def __lt__(self, other):
            # <
            return self != other and not self > other

        @_convert_to_fraction
        def __ge__(self, other):
            # >=
            return self == other or self > other

        @_convert_to_fraction
        def __le__(self, other):
            # <=
            return not self > other

        # решение
        def __radd__(self, other):
            return self + other

        def __rsub__(self, other):
            return Fraction(other) - self

        def __rmul__(self, other):
            return self * other

        def __rtruediv__(self, other):
            return Fraction(other) / self

    """
    a = Fraction(1)
    b = Fraction("2")
    c, d = map(Fraction.reverse, (2 + a, -1 + b))
    print(f"{a} {b} {c} {d}" == "1/1 2/1 1/3 1/1")
    print(f"{a > b} {c > d}" == "False False")
    print(f"{a >= 1} {b >= 1} {c >= 1} {d >= 1}" == "True True False True")


    a = Fraction(1, 2)
    b = Fraction("2/3")
    c, d = map(Fraction.reverse, (3 - a, 2 / b))
    print(f"{a} {b} {c} {d}" == "1/2 2/3 2/5 1/3")
    print(f"{a > b} {c > d}" == "False True")
    print(f"{a >= 1} {b >= 1} {c >= 1} {d >= 1}" == "False False False False")
    """
