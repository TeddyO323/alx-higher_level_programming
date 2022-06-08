#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in range(len(matrix)):
        newMatrix.append([])
        for col in range(len(matrix[row])):
            newMatrix[row].append(matrix[row][col] ** 2)
    return newMatrix
