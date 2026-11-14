# Вариант 21
# Дано целое положительное число. Вывести символы, изображающие цифры этого
# числа (в порядке справа налево).
from input_number import get_int

number = get_int("Введите целое положительно число: ")
if number <= 0:
    print("Ошибка! Число должно быть положительным.")
    exit(1)

symbols = str(number)
invert_symbols = symbols[::-1]

print(invert_symbols)