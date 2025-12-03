#!/usr/bin/python3
from typing import List, Tuple


def read_input(infile: str) -> List[List[int]]:
    output = []
    with open(infile, 'r') as f:
        line = f.readline()
        while line:
            parsed_line = [int(i) for i in list(line.strip())]
            output.append(parsed_line)
            line = f.readline()
    return output
            

def find_max(joltage: List[List[int]]) -> int:
    final_sum = 0
    for bank in joltage:
        first_i = bank.index(max(bank[:-1]))
        first = bank[first_i]
        second = max(bank[first_i+1:])
        out = first * 10 + second
        final_sum += out
    return final_sum


batteries = read_input("./day3/day3_test_data.txt")
# print(batteries)
print(find_max(batteries))
        
        