#!/usr/bin/python3
from typing import List, Tuple

IDS = List[Tuple[int, int]]

def read_input(infile: str) -> IDS:
    with open(infile, 'r') as f:
        ids = [(int(a.split("-")[0]), int(a.split("-")[1])) for a in f.readline().strip().split(",")]
    return ids

ids = read_input(infile="./day2/test_data_day2.txt")

def run_control(ids: IDS) -> int:
    invalid = []
    for start, end in ids:
        invalid += check_id(start, end)
    return invalid

def check_id(start, end):
    possibilities = range(start, end + 1)
    out = []
    for i in possibilities:
        str_id = str(i)
        if len(str_id) % 2 != 0:
            continue
        k = len(str_id) // 2
        if str_id[:k] == str_id[k:]:
            out.append(i)
    return out
            
print(sum(run_control(ids)))