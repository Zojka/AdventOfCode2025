#!/usr/bin/python3
from typing import Tuple, List, Set

def read_input(infile: str) -> List[Tuple[int, int]]:
    fresh_ranges = []
    ingredients = []
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
    return fresh_ranges


def check_freshness(fresh_ranges: List[Tuple[int, int]]) -> int:
    counted = 0
    counted += fresh_ranges[0][1]+ 1 - fresh_ranges[0][0]
    processed_ranges = [fresh_ranges[0]]
    for start, end in fresh_ranges[1:]:
        overlap = check_overlap((start, end), processed_ranges) 
        if overlap == 0:
            current = end + 1 - start
        else:
            current = end + 1 - start - overlap
        print(start, end, counted, current)
        counted += current
        processed_ranges.append((start, end))
    return counted

def check_overlap(current_range, processed_ranges):
    final_overlap = 0
    for start, end in processed_ranges:
        
        overlap = max(0, min(end, current_range[1]) - max(start, current_range[0]) + 1)
        final_overlap += overlap
    return overlap

fresh = read_input("day5_sample_data.txt")
counted = check_freshness(fresh)
print(counted)