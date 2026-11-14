# Вариант 21
# Дано множество A из N точек на плоскости и точка B (точки заданы своими
# координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
# Расстояние R между точками с координатами (x 1, y 1) и (x2 , у2) вычисляется по
# формуле:
# R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.

from math import sqrt
from input_number import get_int
from Point.point_operations import get_point, distance_sqr

points = []
point_b = get_point("Введите точку B")

n = get_int("Введите количество точек (N): ")
if n <= 0:
    print("Ошибка! N должен быть больше 0.")
    exit(1)

for i in range(n):
    points.append(get_point(f"Введите точку #{i}"))

min_distance_sqr = -1
closest_point = None

for i in points:
    d = distance_sqr(i, point_b)

    if d < min_distance_sqr or min_distance_sqr == -1:
        min_distance_sqr = d
        closest_point = i

print(f"Точка: {closest_point}. Расстояние до точки B {point_b}: {sqrt(min_distance_sqr)}")
