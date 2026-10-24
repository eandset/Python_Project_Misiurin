# Вариант 21.
# Даны 2 числа. Вывести порядок меньшего из них.

while True:
    try:
        first_number = float(input("Введити первое число: "))
    except ValueError:
        print("Ошибка! Не число.")
        continue
    try:
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Не число.")
        continue

    if first_number < second_number:
        print(1)
    elif second_number < first_number:
        print(2)
    else:
        print("Числа равны")
