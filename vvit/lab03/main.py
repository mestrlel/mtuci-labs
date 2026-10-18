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

value = 10
def example():
    value = 20
    message = 'Внутри функции:'
    print(message, value)
example()
print("Снаружи функции:", value)
 # print(message) ошибка возникает потому что  переменная определенна только внутри функции
 