import time
from pprint import pprint

# -------------------------------
# Возведение чисел в степень
# -------------------------------
def powers(*args, power=2):
    return [x ** power for x in args]

# -------------------------------
# Проверка на простое число
# -------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# -------------------------------
# Фильтрация чисел по типу
# -------------------------------
def filter_numbers(numbers, mode='even'):
    if mode == 'even':
        return [x for x in numbers if x % 2 == 0]
    elif mode == 'odd':
        return [x for x in numbers if x % 2 != 0]
    elif mode == 'prime':
        return [x for x in numbers if is_prime(x)]
    else:
        raise ValueError("mode должен быть: 'even', 'odd' или 'prime'")

# -------------------------------
# Декоратор для замера времени
# -------------------------------
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ Функция '{func.__name__}' выполнена за {end - start:.6f} секунд")
        return result
    return wrapper

# -------------------------------
# Декоратор для отображения вложенных вызовов
# -------------------------------
def trace(func):
    indent = "  "
    level = 0

    def wrapper(n):
        nonlocal level
        print(f"{indent * level}--> {func.__name__}({n})")
        level += 1
        result = func(n)
        level -= 1
        print(f"{indent * level}<-- {func.__name__}({n}) == {result}")
        return result
    return wrapper

# -------------------------------
# Рекурсивная функция Фибоначчи
# -------------------------------
@trace
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



# -------------------------------
# Демонстрация работы
# -------------------------------
if __name__ == '__main__':
    print("🔹 Список квадратов чисел:")
    pprint(powers(2, 3, 4, 5))

    print("\n🔹 Список чисел, возведённых в 3-ю степень:")
    pprint(powers(2, 3, 4, 5, power=3))

    sample_list = list(range(1, 20))

    print("\n🔹 Чётные числа:")
    pprint(filter_numbers(sample_list, mode="even"))

    print("\n🔹 Нечётные числа:")
    pprint(filter_numbers(sample_list, mode="odd"))

    print("\n🔹 Простые числа:")
    pprint(filter_numbers(sample_list, mode="prime"))

    print("\n🔹 Фибоначчи с отображением рекурсии (до 5):")
    fibonacci(5)

    print("\n🔹 Замер времени на вычисление квадратов:")

    @timing
    def test_powers():
        return powers(*range(1, 10_000))


    test_powers()