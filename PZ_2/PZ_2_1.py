# Вариант 21.
# Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).

def is_invalid_number(n: int) -> bool:
    return n > 999 or n < 100

while True:
    try:
        number = int(input("Введите трёхзначное число: "))

        if is_invalid_number(number):
            print("Некорректный ввод! По заданию нужно ввести положительное трёхзначное число! Попробуйте снова!")
            continue

        first_symbol = number // 100
        second_symbol = number % 100 // 10
        third_symbol = number % 10

        result = (first_symbol * 100
                  + third_symbol * 10
                  + second_symbol)

        print(result)

    except ValueError:
        print("Ошибка! Введите целочисленное число!")
