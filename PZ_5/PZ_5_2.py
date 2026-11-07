# Вариант 21
# Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
# или отрицательного параметра A функция возвращает 0. С помощью этой функции
# найти степени AP, BP, CP, если даны числа P, A, B, C.

import math

def power1(left:float, right:float) -> float:
    if left <= 0:
        return 0.0

    return math.exp(right * math.log(left, math.e))

p = float(input("Введите p: "))
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

print(f"AP: {power1(a, p).__round__(4)}")
print(f"BP: {power1(b, p).__round__(4)}")
print(f"CP: {power1(c, p).__round__(4)}")
