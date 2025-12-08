#!/usr/bin/env python3

from typing import List, Tuple
from scipy.spatial.distance import cdist
import numpy as np
from math import prod

def load_data(infile: str) -> List[List[int]]:
    out = []
    with open(infile, 'r') as f:
        line = f.readline().strip()
        while line:
            out.append([int(i) for i in line.split(",")])
            line = f.readline().strip()
    return out


def compute_distances(indata: List[List[int]]) -> List[List[int]]:
    distances = cdist(indata, indata, metric="euclidean")
    return np.array(distances)


def create_circuits(distances: List[List[int]], points: List[List[int]]):
    circuits = [[i] for i in range(len(points))]
    
    while len(circuits) > 1:
        masked = np.ma.masked_equal(distances, 0)
        flat_idx = masked.argmin()
        coords = np.unravel_index(flat_idx, distances.shape)
        distances[coords] = 0
        distances[coords[::-1]] = 0
        temp_circuits = add_new_connection(coords, circuits)
        circuits = merge_circuits(temp_circuits)
    last1 = points[coords[0]]
    last2 = points[coords[1]]
    return last1[0] * last2[0]


def add_new_connection(new_connection: Tuple[int, int], circuits: List[List[int]]):
    
    if not circuits:
        return [list(new_connection)]
    
    for i, connection in enumerate(circuits):
        if new_connection[0] in connection and new_connection[1] in connection:
            return circuits
        
        elif new_connection[0] in connection and new_connection[1] not in connection:
            connection.append(new_connection[1])
            circuits[i] = connection
        
        elif new_connection[1] in connection and new_connection[0] not in connection:
            connection.append(new_connection[0])
            circuits[i] = connection
            
        else: # create a new circuit
            circuits.append(list(new_connection))
        
        return circuits
     
        
def merge_circuits(connections: List[List[int]]):
    lists = [set(x) for x in connections]
    out = []

    while lists:
        first = lists.pop(0)
        merged = True
        while merged:
            merged = False
            for s in lists[:]:
                if first & s:
                    first |= s
                    lists.remove(s)
                    merged = True
        out.append(sorted(first))
    return out
        
    
    
indata = load_data("day8_test_data.txt")
distances = compute_distances(indata)
print(create_circuits(distances, indata))