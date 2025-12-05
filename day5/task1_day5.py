#!/usr/bin/python3
from typing import Tuple, List, Set

def read_input(infile: str) -> Tuple[Set[int], Set[int]]:
    fresh_ranges = []
    ingredients = []
    with open(infile, 'r') as f:
        lines = f.readlines()
        for raw_line in lines:
            line = raw_line.strip()
            if not line:
                continue
            if '-' in line:
                parts = line.split('-')
                start, end = map(int, parts)
                fresh_ranges.append((start, end))
            else:
                ingredients.append(int(line))
    return (fresh_ranges, ingredients)



def check_freshness(fresh_ranges: List[Tuple[int, int]], ingredients: List[int]) -> int:
    counted = 0
    for ing in ingredients:
        if any(start <= ing <= end for start, end in fresh_ranges):
            counted += 1
    return counted


fresh, ingredients = read_input("day5_test_data.txt")
counted = check_freshness(fresh, ingredients)
print(counted)