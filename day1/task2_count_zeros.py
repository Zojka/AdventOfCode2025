#!/usr/bin/python3
from typing import List, Tuple
from math import floor, ceil

Steps = List[Tuple[int, int]]

def read_input(infile: str) -> Steps:
    steps = []
    with(open(infile, "r") as f):
        line = f.readline().strip()
        while line:
            if line[0] == "R":
                direction = 1
            else:
                direction = -1
            steps.append((direction, int(line[1:])))
            line = f.readline()
    return steps


def take_a_step(step: int, direction: int, current: int) -> Tuple[int, int]:
    i = 0
    counter = 0
    while i < step:
        i +=1
        current += direction
        if current == 100:
            current = 0
        elif current == -1:
            current = 99
            
        if current == 0:
            counter += 1
    return (current, counter)
          

def rotations(steps: Steps, position: int) -> int:
    times_zero = 0
    for direction, step in steps:
        position, temp = take_a_step(step, direction, position)
        
        times_zero += temp
        print(direction, step, position, times_zero)
    return times_zero

steps = read_input("./day1/test_data.txt")
times_zero = rotations(steps, 50)
print(times_zero)
