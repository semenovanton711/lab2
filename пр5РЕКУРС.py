k = int(input("Введите k: "))

total_sum = 0.0
factorial = 1

for i in range(1, k + 1):
    factorial *= i  # вычисляем i!
    total_sum += 1 / factorial  # добавляем 1/i! к сумме

print(f"Сумма S = {total_sum}")
