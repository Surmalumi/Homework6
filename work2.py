# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).

class Road:
    _length = 0
    _width = 0
    __thickness = 0.05  # перевела см в метры
    __weight_asphalt = 25

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def total(self):
        return self._length * self._width * self.__thickness * self.__weight_asphalt

road = Road(length=5000, width=25)
print(road.total())