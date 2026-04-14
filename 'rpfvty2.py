import math

def calculate_sum_math(k):
    total_sum = 0
    for i in range(1, k + 1):
        total_sum += 1 / math.factorial(i)
    return total_sum

# Пример использования
k = 5
result = calculate_sum_math(k)
print(f"Сумма S при k={k}: {result}")
