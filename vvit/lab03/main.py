# Задание 1

# def greet(name):
#     print(f"Привет {name}")

# def square(number):
#     return number * number

# def max_of_two(a, b):
#     if a >= b:
#         return a
#     else:
#         return b

# greet("Иван")
# greet("Алексей")

# print("Квадрат 5:", square(5))
# print("Квадрат -3:", square(-3))

# print("Большее из 4 и 9:", max_of_two(4, 9))
# print("Большее из 12 и 7:", max_of_two(12, 7))


# Задание 2

# def calculate_rectangle(width, height):
#     return width * height

# def calculate_perimeter(width, height):
#     return 2 * (width + height)

# def describe_rectangle(width, height, unit="см"):
#     print(f"Прямоугольник: {width} × {height} {unit}")

# print("Площадь:", calculate_rectangle(3, 5))
# print("Периметр:", calculate_perimeter(3, 5))

# describe_rectangle(3, 5)
# describe_rectangle(width=2, height=4, unit="м")


# Задание 3

# value = 10
# def example():
#     value = 20
#     message = 'Внутри функции:'
#     print(message, value)
# example()
# print("Снаружи функции:", value)
#  # print(message) ошибка возникает потому что  переменная определенна только внутри функции


# Задание 4. Работа со списками

# Демонстрационный запуск отключён после проверки.
# numbers = [8, 3, 12, -4, 7, 0, 15, 2, 9, 6]
# print('Исходный список:', numbers)
# print('Первый, третий, последний:', numbers[0], numbers[2], numbers[-1])
# numbers[1] = 30
# numbers.append(100)
# print('Удалён элемент:', numbers.pop(3))
# print('Итог:', numbers, 'Количество:', len(numbers))


# Задание 5. Срезы

# Демонстрационный запуск отключён после проверки.
# numbers = list(range(1, 11))
# for label, result in [('Первые три', numbers[:3]), ('Последние три', numbers[-3:]), ('С 3-го по 7-й', numbers[2:7]), ('Каждый второй', numbers[::2]), ('В обратном порядке', numbers[::-1])]:
#     print(label + ':', result)


# Задание 6. Работа с кортежами

# Демонстрационный запуск отключён после проверки.
# measurements = (12, 15, 11, 18, 14, 20, 16, 13)
# print('Первый:', measurements[0], 'Последний:', measurements[-1])
# print('Срез:', measurements[2:5])
# try:
#     measurements[0] = 99
# except TypeError as error:
#     print(type(error).__name__ + ':', error)
# print('Кортеж нельзя изменять поэлементно.')
# first, second = measurements[:2]
# print('Распаковка:', first, second)
# mutable = list(measurements)
# mutable[0] = 99
# measurements = tuple(mutable)
# print('Новый кортеж:', measurements)


# Задание 7. Встроенные функции

# Демонстрационный запуск отключён после проверки.
# numbers = [8, 3, 12, -4, 7, 0, 15, 2, 9, 6]
# print('Количество:', len(numbers), 'Сумма:', sum(numbers))
# print('Минимум:', min(numbers), 'Максимум:', max(numbers))
# print('Среднее:', sum(numbers) / len(numbers))
# print('sorted:', sorted(numbers))
# print('Исходный список после sorted:', numbers)
# result = numbers.sort()
# print('Список после sort:', numbers, 'Возвращённое значение:', result)


# Задание 8. Собственные алгоритмы

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def find_min(numbers):
    if not numbers:
        raise ValueError('Список не должен быть пустым')
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result


def find_max(numbers):
    if not numbers:
        raise ValueError('Список не должен быть пустым')
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


# Демонстрационный запуск отключён после проверки.
# numbers = [8, 3, 12, -4, 7, 0, 15, 2, 9, 6]
# print('Своя сумма / sum:', calculate_sum(numbers), sum(numbers))
# print('Свой минимум / min:', find_min(numbers), min(numbers))
# print('Свой максимум / max:', find_max(numbers), max(numbers))


# Задание 9. Линейный поиск

def find_element(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


# Демонстрационный запуск отключён после проверки.
# numbers = [4, 7, 2, 7, 9]
# print('Список:', numbers)
# print('Индекс первого 7:', find_element(numbers, 7))
# print('Поиск 100:', find_element(numbers, 100))
