class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculator(self):
        weight = self._length * self._width * 25 * 8
        return weight


weight_road_calc = Road(1000, 10)
print(weight_road_calc.calculator() / 1000, 'т')
