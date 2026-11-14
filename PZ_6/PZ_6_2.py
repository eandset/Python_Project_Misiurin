# Вариант 21
# Дан целочисленный список размера N. Если он является перестановкой, то есть
# содержит все числа от 1 до N, то вывести 0; в противном случае вывести номер
# первого недопустимого элемента.

from input_number import get_int, get_float
from typing import Tuple


def get_invalid_index(numbers: list) -> Tuple[bool, int]:
    last = 0
    for i, item in enumerate(numbers):
        if last + 1 != item:
            return False, i

        last += 1

    return True, 0


n = get_int("Введите размер списка (N): ")

if n <= 0:
    print("Ошибка! N должен быть больше 0.")
    exit(1)

numbers = []
for i in range(n):
    numbers.append(get_float(f"Введите число #{i}: "))

is_per, index = get_invalid_index(numbers)
msg = ("Является " if is_per else "Не является ") + "перестановкой"

print(msg, index)