def find_min_cubes_sum(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    cubes = []
    i = 1
    while i ** 3 <= n:
        cubes.append(i ** 3)
        i += 1
    for cube in cubes:
        for j in range(cube, n + 1):
            dp[j] = min(dp[j], dp[j - cube] + 1)
    return dp[n]
def main():
    try:
        n = input("Введите натуральное число N (≤ 10^6): ").strip()
        if not n:
            raise ValueError("Ввод не должен быть пустым.")
        n = int(n)
        if n <= 0:
            raise ValueError("Число должно быть натуральным (больше 0).")
        if n > 10**6:
            raise ValueError("Число не должно превышать 10^6.")
        result = find_min_cubes_sum(n)
        print(f"Минимальное количество слагаемых (кубов): {result}")
    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except OverflowError:
        print("Ошибка: число слишком велико для обработки.")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
if __name__ == "__main__":
    main()
