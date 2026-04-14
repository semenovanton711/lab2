import math

def calculate_with_math_factorial(k):
    total_sum = 0.0
    for i in range(1, k + 1):
        term = 1 / math.factorial(i)
        total_sum += term
    return total_sum
