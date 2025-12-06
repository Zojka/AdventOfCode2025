#!/usr/bin/env python3
import numpy as np
import pandas as pd

def read_input(infile: str):
    table = pd.read_csv(infile, header=None, delim_whitespace=True)
    table_t = table.T
    
    return table_t



def do_math(input_df) -> int:
    num_columns = input_df.columns[:-1]
    input_df[num_columns] = input_df[num_columns].astype(int)
    flag_columns = input_df.columns[-1]
    input_df["result"] = input_df.apply(
        lambda row: row[num_columns].sum()
        if row[flag_columns] == "+"
        else row[num_columns].prod(),
        axis =1
    )
    return input_df, input_df["result"].sum()

matrix = read_input("day6_sample_data.txt")
print(matrix)
print(do_math(matrix))