# Вариант 21
# Дан целочисленный список размера N. Если он является перестановкой, то есть
# содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
# первого недопустимого элемента.

from random import randint, shuffle
from input_number import get_int

def find_invalid_element(numbers: list[int]) -> int:
    n = len(numbers)
    pattern = []

    for i in range(n + 1):
        pattern.append(i)

    for index, num in enumerate(numbers):
        if num not in pattern:
            return index
        pattern.remove(num)

    return 0

n = get_int("Введите размер списка (N): ")
if n <= 0:
    print("Ошибка! N должен быть больше 0.")
    exit(1)

numbers = []
for i in range(n):
    random_int = randint(1, n)
    numbers.append(random_int)

print("Рандомные числа:")
print(f"#{find_invalid_element(numbers)}")
print(numbers)

print()
print("Целевой список:")

numbers = list(range(1, n + 1))
shuffle(numbers)

print(f"#{find_invalid_element(numbers)}")
print(numbers)