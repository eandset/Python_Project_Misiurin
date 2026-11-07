# Вариант 21
# Составить функцию, которая выполнит суммирования числового ряда.

res = 0.0

exit_key = "exit"
command = input(f"Введите число ({exit_key} для завершения): ")

while command != exit_key:
    try:
        number = float(command)
        res += number
    except ValueError:
        print(f"Ошибка! Введите число или {exit_key} для завершения")

    command = input(f"Введите число ({exit_key} для завершения): ")

print(f"Сумма всех введёных чисел: {res}")
