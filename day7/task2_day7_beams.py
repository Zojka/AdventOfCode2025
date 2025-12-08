#!/usr/bin/env python3
from typing import List

def read_input(infile: str) -> List[List[str]]:
    output = []
    with open(infile, 'r') as f:
        line = list(f.readline().strip())
        while line:
            output.append(line)
            line = list(f.readline().strip())
    return output


def run_tachyon_beam(manifold: List[List[str]]) -> int:
    beam_positions = [manifold[0].index("S")]
    new_manifold = [manifold[0]]
    for row in manifold[1:]:
        if "^" in row:
            splitters = [i for i, value in enumerate(row) if value == '^' and i in beam_positions]
            beam_positions = split_beams(beam_positions, splitters)
        temp_row = row.copy()
        for i in beam_positions:
            temp_row[i] = "|"
        new_manifold.append(temp_row)
    return new_manifold
        
        
def split_beams(beam_positions: List[int], splitters: List[int]):
    new_beam_positions = []
    for split in splitters:
        new_splits = [split - 1, split + 1]
        new_beam_positions += new_splits
        beam_positions.remove(split)
    final_beams = list(set(beam_positions + new_beam_positions))
    return final_beams


def count_paths(manifold: List[List[str]]) -> int:
    manifold = run_tachyon_beam(manifold)
    previous = manifold[0].copy()
    previous = [0 if i == "." else 1 for i in previous  ]
    current = [0] * len(previous)
    print(previous)
    for row in manifold[1:]:
        for i in range(len(row)):
            if row[i] == "|":
                if i-1>=0 and row[i-1] == "^":
                    current[i] += previous[i-1]
                if i+1 < len(row) and row[i+1] == "^":
                    current[i] += previous[i+1]
                current[i] += previous[i]
            if row[i] == "^":
                current[i] = 0             
        print(current)
        previous = current
        current = [0] * len(previous)        
    return sum(previous)
              

manifold = read_input("./day7/day7_test_data.txt")
print(count_paths(manifold))