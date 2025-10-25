#!/usr/bin/env python3

def print_squares(start, end):
    """Print squares of integers from start to end (inclusive)"""
    for i in range(start, end + 1):
        print(f"{i}^2 = {i**2}")

if __name__ == "__main__":
    print("Squares of integers from 1 to 65:")
    print_squares(1, 65)