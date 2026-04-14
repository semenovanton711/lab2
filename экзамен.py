def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def calculate_sum_recursive(k):
    total_sum = 0
    for i in range(1, k + 1):
        total_sum += 1 / factorial_recursive(i)
    return total_sum

# Пример использования
k = 5
result = calculate_sum_recursive(k)
print(f"Сумма S при k={k}: {result}")
