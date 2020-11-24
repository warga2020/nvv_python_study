class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count <= other.count:
            raise Exception('Error! Subtraction result is negative')
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(round(self.count / other.count))

    def make_order(self, row_size):
        x = divmod(self.count, row_size)
        return (('*' * row_size + '\n') * x[0] + '*' * x[1]).rstrip()


a = Cell(13)
b = Cell(7)
print((a + b).make_order(9) + '\n')
print((a - b).make_order(4) + '\n')
try:
    print((b - a).make_order(4) + '\n')
except Exception as e:
    print(str(e) + '\n')
print((a * b * b).make_order(111) + '\n')
print((a / b).make_order(11) + '\n')

