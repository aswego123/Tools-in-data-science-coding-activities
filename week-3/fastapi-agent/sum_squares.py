#!/usr/bin/env python3

def sum_of_squares(n):
    """Calculate the sum of squares from 1 to n."""
    return sum(i**2 for i in range(1, n + 1))

if __name__ == "__main__":
    n = 65
    result = sum_of_squares(n)
    print(f"The sum of squares from 1 to {n} is: {result}")