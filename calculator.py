import argparse
import ast
import json


def calculate_payments(p: int, A: list) -> list:
    allocations = []  # List of ints

    return allocations


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lumpsum", type=int)
    parser.add_argument("table", type=str)
    args = parser.parse_args()
    lump_sum = args.lumpsum
    tablestr = args.table
    table = ast.literal_eval(
        tablestr
    )  # Evaluate string representation of python matrix into actual matrix
    print(f"Received:\nPayment: {lump_sum}\nLoans:\n{json.dumps(table, indent=4)}")
    allocations = calculate_payments(lump_sum, table)
    print(f"Allocations: {allocations}")
