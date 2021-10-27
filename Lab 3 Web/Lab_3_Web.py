from sys import stdin
from copy import deepcopy
import numpy as np
class Matrix:
    def __init__(self, list_of_lists): #инициализация
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):#вывод в консоль
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)
    def __getitem__(self, idx): #получение элемента
        return self.matrix[idx]

    def __gt__(self, other):#больше
        return np.linalg.det(self.matrix) > np.linalg.det(other.matrix)
    def __eq__(self, other):#равно
        return np.linalg.det(self.matrix) == np.linalg.det(other.matrix)
    def __lt__(self, other):#меньше
        return np.linalg.det(self.matrix) < np.linalg.det(other.matrix)

    def __add__(self, other):#сложение
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __mul__(self, other):#умножение
        result = Matrix([[0,0],[0,0]])
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self[i][k] * other[k][j]
        return result

m1 = Matrix([[1,1],[2,2]])
m2 = Matrix([[1,2],[3,4]])
print("1ая больше, чем 2ая:")
print(m1 > m2)
print("1ая равна 2ой:")
print( m1 == m2)
print("1ая меньше, чем 2ая:")
print( m1 < m2)

print("Сложение:")
print(m1+m2)
print("Умножение:")
print(m1*m2)