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
        dividers = find_all_dividers(len(str_id))
        for di in dividers:
            parts = [str_id[i:i+di] for i in range(0, len(str_id), di)]
            if len(set(parts)) == 1:
                out.append(i)
                break
    return out

def find_all_dividers(number: int):
    i = 1
    dividers = []
    while i < number:
        if number % i == 0:
            dividers.append(i)
        i += 1
    return dividers


print(sum(run_control(ids)))
