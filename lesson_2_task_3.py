
import math


def square(Сторона):
    Площадь = Сторона * Сторона
    return math.ceil(Площадь) if not isinstance(Сторона, int) else Площадь


print(f"Сторона 5: {square(5)}")
