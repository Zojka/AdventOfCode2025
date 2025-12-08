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
    split_counter = 0
    beam_positions = [manifold[0].index("S")]
    all_beam_positions = beam_positions.copy()
    for row in manifold[1:]:
        if "^" in row:
            splitters = [i for i, value in enumerate(row) if value == '^' and i in beam_positions]
            beam_positions, temp_counter = split_beams(beam_positions, splitters)
            split_counter += temp_counter
    return split_counter
        
        
def split_beams(beam_positions: List[int], splitters: List[int]):
    split_counter = 0
    new_beam_positions = []
    for split in splitters:
        new_splits = [split - 1, split + 1]
        split_counter += 1
        new_beam_positions += new_splits
        beam_positions.remove(split)
    final_beams = list(set(beam_positions + new_beam_positions))
    return final_beams, split_counter
            

manifold = read_input("day7_test_data.txt")
print(run_tachyon_beam(manifold))