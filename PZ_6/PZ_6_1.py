# Вариант 21
# Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму всех
# элементов списка, кроме элементов с номерами от K до L включительно.

from input_number import get_int, get_float


def get_errors(n: int, l: int, k: int) -> list:
    msg = []

    if n <= 1:
        msg.append("N должно быть больше 1")
    if l >= n:
        msg.append("L должно быть меньше N")
    if k >= l:
        msg.append("K должно быть меньше L")

    return msg


n = get_int("Введите размер списка (N): ")
l = get_int("Введите L (L < N): ")
k = get_int("Введите K (K < L): ")

errors = get_errors(n, l, k)
if len(errors) != 0:
    print(f"Ошибка! {errors}.")
    exit(1)

numbers = []
for i in range(n):
    numbers.append(get_float(f"Введите число #{i}: "))

res = 0
for i, item in enumerate(numbers):
    if i < k or i > l:
        res += item

print(f"Сумма: {res}")
