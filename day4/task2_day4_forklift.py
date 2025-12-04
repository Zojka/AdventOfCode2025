#!/usr/bin/python3

from numpy.typing import NDArray
import numpy as np

def read_table(infile: str) ->  list:
    with open(infile, "r") as f:
        lines = [['.'] + list(line.strip()) + ['.'] for line in f]
    first = ['.' for l in lines[0]]
    return [first] +lines + [first]


def remove_tps(matrix: list) -> list:
    removed = 0
    temp_removed = 1
    while temp_removed != 0:
        temp_removed = 0
        temp_removed, marked = check_the_wall(matrix)
        removed += temp_removed
        for i,j in marked:
            matrix[i][j] = '.'
    return removed


def check_the_wall(matrix: list):
    how_many = 0 
    marked = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0 or i == len(matrix):
                continue
            if j == 0 or j == len(matrix):
                continue
        
            if matrix[i][j] == "@":
                counter = 0
                for n in [-1, 0, 1]:
                    for m in [-1, 0, 1]:
                        if m == 0 and n ==0:
                            continue
                        else:
                            if matrix[i+n][j+m] == '@':
                                counter += 1
                if counter < 4:
                    how_many += 1
                    marked.append((i, j))
    return how_many, marked
            
                
                
            

infile = "./day4/day4_test_data.txt"
tp_square = read_table(infile)
print(np.array(tp_square))
removed = remove_tps(tp_square)
print(removed)