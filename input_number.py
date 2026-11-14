def get_int(msg: str = "", msg_error: str = "Ошибка! Ожидается целочисленное число.") -> int:
    i = input(msg)

    while type(i) != int:
        try:
            i = int(i)
        except ValueError:
            print(msg_error)
            i = input(msg)

    return i


def get_float(msg: str = "", msg_error: str = "Ошибка! Ожидается вещественное число.") -> float:
    i = input(msg)

    while type(i) != float:
        try:
            i = float(i)
        except ValueError:
            print(msg_error)
            i = input(msg)

    return i

