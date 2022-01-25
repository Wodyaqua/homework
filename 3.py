class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return str(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums > other.nums:
            return str(self.nums - other.nums)
        else:
            return 'Error'

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __truediv__(self, other):
        if other.nums > 0:
            return str(self.nums / other.nums)


cell = Cell(17)
print(cell.make_order(5))
cell_2 = Cell(24)
# print(cell)
# print(cell_2)
print(cell + cell_2)
print(cell_2 - cell)
# print(cell * cell_2)
# print(cell_2 / cell)
