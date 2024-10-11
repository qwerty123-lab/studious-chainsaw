import random

class Matrix:
    def __init__(self, rows, cols, fill_method):
        self.rows = rows
        self.cols = cols
        self.fill_method = fill_method
        self.matrix = self.create_matrix()

    def create_matrix(self):
        if self.fill_method == 1:
            return [[self.fill_rule_1(i, j) for j in range(self.cols)] for i in range(self.rows)]
        elif self.fill_method == 2:
            return [[self.fill_rule_2(i, j) for j in range(self.cols)] for i in range(self.rows)]
        elif self.fill_method == 3:
            return [[self.fill_random() for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            raise ValueError("Неверный метод заполнения")

    def fill_rule_1(self, i, j):
        return i + j

    def fill_rule_2(self, i, j):
        return i * j

    def fill_random(self):
        return random.randint(0, 100)  

    def display(self):
        for row in self.matrix:
            print(row)

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
fill_method = int(input("Выберите метод заполнения (1 - i+j, 2 - i*j, 3 - случайные значения): "))

matrix = Matrix(rows, cols, fill_method)
matrix.display()
