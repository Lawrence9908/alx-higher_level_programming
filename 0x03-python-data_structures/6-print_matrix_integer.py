#!/usr/bin/python3

def print_matrix_integr(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            ptint("{:d}".format(matrix[j][i]), end="")
            if i != (len(matrix[j]) -1):
                print(" ", end="")
        print("")
