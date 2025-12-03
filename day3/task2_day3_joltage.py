#!/usr/bin/python3
from typing import List, Tuple
import heapq


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
        i = 0
        numbers = []
        curr_index = bank.index(max(bank[:-11]))
        numb = bank[curr_index]
        numbers.append(numb)
        while i < 11:
            ind = -(11-i-1)
            if ind == 0:
                ind = len(bank)
            temp_fragment = bank[curr_index + 1:ind]
            print(temp_fragment)
            temp_index = temp_fragment.index(max(temp_fragment))
            curr_index = curr_index + temp_index + 1
            numb = bank[curr_index]
            numbers.append(numb)
            i += 1
            
        temp_numbers = int(''.join([str(s) for s in numbers]))
        final_sum += temp_numbers
    return final_sum

batteries = read_input("./day3/day3_sample_data.txt")
# print(batteries)
print(find_max(batteries))