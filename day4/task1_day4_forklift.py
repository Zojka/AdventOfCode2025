#!/usr/bin/python3

from numpy.typing import NDArray
import numpy as np

def read_table(infile: str) ->  list:
    with open(infile, "r") as f:
        lines = [['.'] + list(line.strip()) + ['.'] for line in f]
    first = ['.' for l in lines[0]]
    return [first] +lines + [first]


def check_the_wall(matrix: list) -> int:
    how_many = 0 
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
    return how_many
            
                
                
            

infile = "./day4/day4_test_data.txt"
tp_square = read_table(infile)
print(np.array(tp_square))
helper = check_the_wall(tp_square)
print(helper)