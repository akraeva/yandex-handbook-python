# Yandex / Хендбуки / Основы Python
# 5.3. Модель исключений Python. Try, except, else, finally. Модули

import hashlib


def func(*args): ...


def p_5_3_a():
    """
    Вашему решению будет предоставлена функция func, которая не имеет
    параметров и результата. Однако во время её исполнения может
    произойти одна из ошибок: ValueError, TypeError или SystemError.
    Вызовите её, обработайте ошибку и выведите её название.
    Если ошибка не произойдёт, выведите сообщение "No Exceptions".
    """

    try:
        func()
    except (ValueError, TypeError, SystemError) as e:
        print(type(e).__name__)
    else:
        print("No Exceptions")


def p_5_3_b():
    """
    Вашему решению будет предоставлена функция func, которая принимает
    два позиционных параметра и производит с ними некую математическую
    операцию. Предложите вызов функции, который гарантированно породит
    ошибку внутри функции.
    Примечание Если ошибка произойдёт внутри функции, то она будет
    перехвачена и обработана. Если же она произойдет в вашем коде,
    то программа будет завершена с ошибкой.
    """

    func(True, func)


def p_5_3_с():
    """
    Вашему решению будет предоставлена функция func, которая на этот
    раз принимает неограниченное число позиционных параметров и
    производит с ними некую операцию приведения типа.
    Предложите вызов функции, который гарантированно породит ошибку
    внутри функции.
    """

    class Crash:
        def __repr__(self) -> str:
            raise Exception()

    func(Crash())


def p_5_3_d():
    """
    Напишите функцию only_positive_even_sum, которая принимает два
    параметра и возвращает их сумму.
    - Если один из параметров не является целым числом,
      то следует вызвать исключение TypeError.
    - Если один из параметров не является положительным чётным числом,
      то следует вызвать исключение ValueError.
    Примечание Ваше решение должно содержать только функции.
    В решении не должно быть вызовов требуемых функций.
    """

    def only_positive_even_sum(num1, num2):
        if not all(isinstance(n, int) for n in (num1, num2)):
            raise TypeError("Вызвано исключение TypeError")
        if not all(n > 0 and n % 2 == 0 for n in (num1, num2)):
            raise ValueError("Вызвано исключение ValueError")
        return num1 + num2


def p_5_3_e():
    """
    Когда-то вы уже писали функцию merge, которая производит
    слияние двух отсортированных кортежей.
    Давай-те её немного переработаем.
    Введём систему проверок:
    - если один из параметров не является итерируемым объектом,
      то вызовите исключение StopIteration;
    - если значения входных параметров содержат «неоднородные» данные,
      то вызовите исключение TypeError;
    - если один из параметров не отсортирован,
      то вызовите исключение ValueError.
    Проверки следует проводить в указанном порядке.
    Если параметры прошли все проверки, верните итерируемый объект,
    являющийся слиянием двух переданных.
    Примечание В решении не должно быть вызовов требуемых функций.
    """

    def merge(arr1, arr2):
        try:
            iter(arr1)
            iter(arr2)
        except TypeError:
            raise StopIteration("Вызвано исключение StopIteration")

        if len({type(a) for a in arr1} | {type(b) for b in arr2}) != 1:
            raise TypeError("Вызвано исключение TypeError")

        if tuple(arr1) != tuple(sorted(arr1)) or tuple(arr2) != tuple(sorted(arr2)):
            raise ValueError("Вызвано исключение ValueError")

        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return tuple(result)


def p_5_3_f():
    """
    В одной из первых лекций вы уже решали задачу о поиске корней
    квадратного уравнения. Давайте модернизируем её.
    Напишите функцию find_roots, принимающую три параметра:
    коэффициенты уравнения и возвращающую его корни в виде
    кортежа из двух значений.
    Так же создайте два собственных исключения
    NoSolutionsError и InfiniteSolutionsError,
    которые будут вызваны в случае отсутствия и бесконечного
    количества решений уравнения соответственно.
    Если переданные коэффициенты не являются рациональными
    числами, вызовите исключение TypeError.
    Примечание В решении не должно быть вызовов требуемых функций.
    """
    # кортеж должен быть отсортирован, как говорилось в задаче 2.2(q)


class NoSolutionsError(Exception): ...


class InfiniteSolutionsError(Exception): ...


def find_roots(a, b, c):
    if not all(isinstance(x, (float, int)) for x in (a, b, c)):
        raise TypeError("Вызвано исключение TypeError")
    if a == b == c == 0:
        raise InfiniteSolutionsError("Вызвано исключение InfiniteSolutionsError")
    if a == b == 0:
        raise NoSolutionsError("Вызвано исключение NoSolutionsError")
    if a == 0:
        x = -c / b
        return x, x
    d = b * b - 4 * a * c
    if d < 0:
        raise NoSolutionsError("Вызвано исключение NoSolutionsError")
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    return tuple(sorted((x1, x2)))


def p_5_3_g():
    """
    При регистрации в различных сервисах пользователи вводят
    большое количество информации. Правильное заполнение полей
    — важная часть работы программы, поэтому формы снабжают
    системами валидации данных.
    Напишите функцию name_validation, которая принимает один
    позиционный аргумент — фамилию или имя.
    Если параметр не является строкой, то вызовите
    исключение TypeError.
    А также разработайте собственные ошибки:
    - CyrillicError — вызывается, если значение не состоит
      только из кириллических букв;
    - CapitalError — вызывается, если значение не начинается с
      заглавной буквы или найдена заглавная буква не в начале значения.
    Обработка ошибок должна происходить в порядке, указанном в задании.
    В случае успешного выполнения, функция должна вернуть
    переданный параметр без изменений.
    """

    class CyrillicError(Exception): ...

    class CapitalError(Exception): ...

    def name_validation(name):
        if not isinstance(name, str):
            raise TypeError("Вызвано исключение TypeError")
        cyrillic = "".join(chr(n) for n in range(ord("а"), ord("я") + 1)) + "ё"
        if not all(ch.lower() in cyrillic for ch in name):
            raise CyrillicError("Вызвано исключение CyrillicError")
        if name[0].islower() or (len(name) > 1 and name[1:] != name[1:].lower()):
            raise CapitalError("Вызвано исключение CapitalError")
        return name

    # print(name_validation("user"))
    # print(name_validation("иванов"))


def p_5_3_h():
    """
    Продолжим реализацию системы валидации.
    Напишите функцию username_validation, которая принимает
    один позиционный аргумент — имя пользователя:
    Если параметр не является строкой, то вызовите исключение TypeError.
    А также разработайте собственные ошибки:
    - BadCharacterError — вызывается, если значение состоит
      не только из латинских букв, цифр и символа нижнего подчёркивания;
    - StartsWithDigitError — вызывается, если значение начинается с цифры.
    Обработка ошибок должна происходить в порядке, указанном в задании.
    В случае успешного выполнения, функция должна вернуть
    переданный параметр без изменений.
    Примечание В решении не должно быть вызовов требуемых функций.
    """

    class BadCharacterError(Exception): ...

    class StartsWithDigitError(Exception): ...

    def username_validation(username):
        if not isinstance(username, str):
            raise TypeError("Вызвано исключение TypeError")
        symbols = "".join(chr(n) for n in range(ord("a"), ord("z") + 1)) + "_"
        nums = "".join(str(n) for n in range(0, 10))
        if not all(ch.lower() in symbols + nums for ch in username):
            raise BadCharacterError("Вызвано исключение BadCharacterError")
        if username[0].isdigit():
            raise StartsWithDigitError("Вызвано исключение StartsWithDigitError")
        return username


def p_5_3_i():
    """
    Используйте две предыдущих функции валидации и напишите
    функцию user_validation, которая принимает именованные аргументы:
    - last_name — фамилия;
    - first_name — имя;
    - username — имя пользователя.
    Если функции был передан неизвестный параметр или не передан
    один из обязательных, то вызовите исключение KeyError.
    Если один из параметров не является строкой,
    то вызовите исключение TypeError.
    Обработка данных должна происходить в порядке:
    фамилия, имя, имя пользователя.
    Если поле заполнено верно, функция возвращает
    словарь с данными пользователя.
    """

    class CyrillicError(Exception): ...

    class CapitalError(Exception): ...

    class BadCharacterError(Exception): ...

    class StartsWithDigitError(Exception): ...

    def name_validation(name):
        if not isinstance(name, str):
            raise TypeError("Вызвано исключение TypeError")
        cyrillic = "".join(chr(n) for n in range(ord("а"), ord("я") + 1)) + "ё"
        if not all(ch.lower() in cyrillic for ch in name):
            raise CyrillicError("Вызвано исключение CyrillicError")
        if name[0].islower() or (len(name) > 1 and name[1:] != name[1:].lower()):
            raise CapitalError("Вызвано исключение CapitalError")
        return name

    def username_validation(username):
        if not isinstance(username, str):
            raise TypeError("Вызвано исключение TypeError")
        symbols = "".join(chr(n) for n in range(ord("a"), ord("z") + 1)) + "_"
        nums = "".join(str(n) for n in range(0, 10))
        if not all(ch.lower() in symbols + nums for ch in username):
            raise BadCharacterError("Вызвано исключение BadCharacterError")
        if username[0].isdigit():
            raise StartsWithDigitError("Вызвано исключение StartsWithDigitError")
        return username

    def user_validation(**kwargs):
        if len(kwargs) != 3:
            raise KeyError("Вызвано исключение KeyError")
        try:
            ln = name_validation(kwargs["last_name"])
            fn = name_validation(kwargs["first_name"])
            un = username_validation(kwargs["username"])
        except TypeError:
            raise TypeError("Вызвано исключение TypeError")
        else:
            return {"last_name": ln, "first_name": fn, "username": un}

    """
    print(
        user_validation(last_name="Иванов", first_name="Иван", username="ivanych45")
        == {"last_name": "Иванов", "first_name": "Иван", "username": "ivanych45"}
    )
    try:
        print(
            user_validation(
                last_name="Иванов",
                first_name="Иван",
                username="ivanych45",
                password="123456",
            )
        )
    except KeyError:
        print("True")
"""


def p_5_3_j():
    """
    После того, как пользователь ввёл свои данные в требуемом
    формате, можно позаботиться и о пароле.
    Напишите функцию password_validation, которая принимает
    один позиционный параметр — пароль,
    и следующие именованные параметры:
    - min_length — минимальная длина пароля, по умолчанию 8;
    - possible_chars — строка символов, которые могут быть
      в пароле, по умолчанию латинские буквы и цифры;
    - at_least_one — функция возвращающая логическое значение,
      по умолчанию str.isdigit.
    Если переданный позиционный параметр не является строкой,
    вызовите исключение TypeError.

    А так же реализуйте собственные исключения:
    - MinLengthError — вызывается, если пароль меньше заданной длины;
    - PossibleCharError — вызывается, если в пароле
      используется недопустимый символ;
    - NeedCharError — вызывается, если в пароле не найдено
      ни одного обязательного символа.
    Проверка условий должна происходить в порядке указанном в задании.

    Так как, хороший разработчик никогда не хранит пароли в
    открытом виде, функция, в случае успешного завершения,
    возвращает хеш пароля. Для этого воспользуйтесь функцией
    sha256 из пакета hashlib и верните его шестнадцатеричное представление.
    """

    # import hashlib

    class MinLengthError(Exception): ...

    class PossibleCharError(Exception): ...

    class NeedCharError(Exception): ...

    def password_validation(
        password, min_length=8, possible_chars=None, at_least_one=str.isdigit
    ):
        if not possible_chars:
            symbols = "".join(chr(n) for n in range(ord("a"), ord("z") + 1))
            nums = "".join(str(n) for n in range(0, 10))
            possible_chars = symbols + symbols.upper() + nums
        if not isinstance(password, str):
            raise TypeError("Вызвано исключение TypeError")
        if len(password) < min_length:
            raise MinLengthError("Вызвано исключение MinLengthError")
        if not all(ch in possible_chars for ch in password):
            raise PossibleCharError("Вызвано исключение PossibleCharError")
        if not any(at_least_one(ch) for ch in password):
            raise NeedCharError("Вызвано исключение NeedCharError")
        pass_hash = hashlib.new("sha256")
        pass_hash.update(password.encode())
        return pass_hash.hexdigest()

    """
    print(
        password_validation("Hello12345")
        == "67698a29126e52a6921ca061082783ede0e9085c45163c3658a2b0a82c8f95a1"
    )

    try:
        print(
            password_validation(
                "$uNri$e_777", min_length=6, at_least_one=lambda char: char in "!@#$%^&*()_"
            )
        )
    except PossibleCharError:
        print("True")
    """
