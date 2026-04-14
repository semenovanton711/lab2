
# Рекурсивный метод
def recurs_sequence(n):
    if n == 1:
        return -3
    return 2 * recurs_sequence(n - 1) + 5
# Вывод первых 30 членов последовательности
print("\n\nРекурсивный метод:")
for i in range(1, 31):
    print(recurs_sequence(i), end=" ")