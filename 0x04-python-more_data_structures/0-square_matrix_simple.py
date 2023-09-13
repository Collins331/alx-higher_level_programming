#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in range(len(matrix)):
        square.append([j ** 2 for j in matrix[i]])

    return square
