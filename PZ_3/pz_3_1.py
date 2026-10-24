# Вариант 21.
# Дано трехзначное число. Проверить истинность высказывания: "Все цифры данного числа различны".

def is_invalid_number(n: int) -> bool:
    return n > 999 or n < 100

while True:
    try:
        number = int(input("Введите трехзначное число: "))
    except ValueError:
        print("Ошибка! Введите целое число.")
        continue

    if is_invalid_number(number):
        print("Ошибка! Введите трехзначное число.")
        continue

    first_symbol = number // 100
    second_symbol = number % 100 // 10
    third_symbol = number % 10

    is_different = first_symbol != second_symbol \
                   and first_symbol != third_symbol \
                   and second_symbol != third_symbol

    message = "Истинно" if is_different else "Ложно"

    print("Выражение \"Все цифры данного числа различны\" - " + message)