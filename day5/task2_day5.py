#!/usr/bin/python3
from typing import Tuple, List, Set

def read_input(infile: str) -> List[Tuple[int, int]]:
    fresh_ranges = []
    with open(infile, 'r') as f:
        lines = f.readlines()
        for raw_line in lines:
            line = raw_line.strip()
            if not line:
                break
            if '-' in line:
                parts = line.split('-')
                start, end = map(int, parts)
                fresh_ranges.append((start, end))
    return sorted(fresh_ranges)


def check_freshness(fresh_ranges: List[Tuple[int, int]]) -> int:
    processed_ranges = []
    curr_start, curr_end = fresh_ranges[0]
    for start, end in fresh_ranges[1:]:
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            processed_ranges.append((curr_start, curr_end))
            curr_start, curr_end = start, end
    processed_ranges.append((curr_start, curr_end))
    counted = sum(end + 1 - start for start, end in processed_ranges)
    return counted

fresh = read_input("./day5/day5_test_data.txt")
counted = check_freshness(fresh)
print(counted)