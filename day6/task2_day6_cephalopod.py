#!/usr/bin/env python3
from typing import List, Tuple
import math

def read_input(infile: str)-> List[str]:
    out = []
    with open(infile, 'r') as f:
        file = f.readlines()
        for line in file:
            out.append(line)
    return out

def parse_data(in_table: list) -> Tuple[List[List[int]], List[str]]:
    result = ["".join(chars).strip() for chars in zip(*in_table[:-1])]
    multi = in_table[-1]
    final_result = []
    current = []

    for x in result:
        (final_result.append(current) or (current := [])) if x == "" else current.append(int(x))

    if current:
        final_result.append(current)
    return final_result, multi.split()

def do_math(numbers: List[List[int]], multi: List[str]) -> int:
    summarized = 0
    for i in range(len(multi)):
        if multi[i] == "+":
            summarized += sum(numbers[i])
        else:
            summarized += math.prod(numbers[i])
    return summarized
            
            
in_data = read_input("day6_test_data.txt")
numbers, multi = parse_data(in_data)
print(do_math(numbers, multi))

