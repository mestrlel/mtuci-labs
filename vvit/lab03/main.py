def greet(name):
    print(f"Привет {name}")

def square(number):
    return number * number

def max_of_two(a, b):
    if a >= b:
        return a
    else:
        return b

greet("Иван")
greet("Алексей")

print("Квадрат 5:", square(5))
print("Квадрат -3:", square(-3))

print("Большее из 4 и 9:", max_of_two(4, 9))
print("Большее из 12 и 7:", max_of_two(12, 7))