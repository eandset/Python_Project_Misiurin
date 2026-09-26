# Вариант 21.
# Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков и единиц исходного числа (например, 123 перейдет в 132).

number = int(input("Введите трёхзначное число: "))

first_symbol = number // 100
second_symbol = number % 100 // 10
third_symbol = number % 10

result = (first_symbol * 100
          + third_symbol * 10
          + second_symbol)

print(result)
