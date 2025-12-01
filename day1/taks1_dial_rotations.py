#!/usr/bin/python3
from typing import List, Tuple
from math import floor

Steps = List[Tuple[str, int]]

def read_input(infile: str) -> Steps:
    steps = []
    with(open(infile, "r") as f):
        line = f.readline().strip()
        while line:
            steps.append((line[0], int(line[1:])))
            line = f.readline()
    return steps


def take_a_step(step: int, direction: str, current: int) -> int:
    if direction == "R":
        if current + step > 99:
            temp = ((current + step) % 100)
            return temp
        else:
            return current + step
    else:
        if current - step < 0:
            temp = abs((current - step) % 100)
            return temp
        else:
            return current - step

def rotations(steps: Steps, position: int) -> int:
    times_zero = 0
    for direction, step in steps:
        # print(position, step)
        position = take_a_step(step, direction, position)
        
        if position == 0:
            times_zero += 1
    return times_zero

steps = read_input("./day1/test_data.txt")
times_zero = rotations(steps, 50)
print(times_zero)