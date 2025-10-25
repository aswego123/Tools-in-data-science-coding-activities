#!/usr/bin/env python3

def sum_of_squares(n):
    """Calculate the sum of squares from 1 to n."""
    return sum(i**2 for i in range(1, n + 1))

if __name__ == "__main__":
    result = sum_of_squares(65)
    print(f"The sum of squares from 1 to 65 is: {result}")