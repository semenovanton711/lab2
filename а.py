import sys

sys.setrecursionlimit(200000)  # Увеличиваем лимит рекурсии

MOD = 10 ** 9 + 7


def solve_recursive():
    try:
        # Чтение входных данных
        n = int(input().strip())
        m = int(input().strip())
        arr = []
        for _ in range(n):
            arr.append(int(input().strip()))

        # Кэш для мемоизации: memo[i][prev] = количество способов
        memo = [[-1] * (m + 1) for _ in range(n + 1)]

        def dfs(pos, prev):
            """
            Рекурсивная функция.
            pos - текущая позиция в массиве (0-based)
            prev - предыдущее значение (0 для первой позиции)
            """
            # Базовый случай: дошли до конца массива
            if pos == n:
                return 1

            # Если результат уже в кэше, возвращаем его
            if memo[pos][prev] != -1:
                return memo[pos][prev]

            res = 0

            if arr[pos] != 0:
                # Значение фиксировано
                current = arr[pos]
                # Проверяем, что разница с предыдущим не превышает 1
                if pos == 0 or abs(current - prev) <= 1:
                    res = dfs(pos + 1, current)
            else:
                # Значение неизвестно, перебираем все возможные значения
                start_val = 1
                end_val = m

                if pos > 0:
                    # Ограничиваем диапазон по условию |val - prev| <= 1
                    start_val = max(1, prev - 1)
                    end_val = min(m, prev + 1)

                for val in range(start_val, end_val + 1):
                    res = (res + dfs(pos + 1, val)) % MOD

            # Сохраняем результат в кэш
            memo[pos][prev] = res
            return res

        # Запускаем рекурсию
        result = dfs(0, 0) % MOD
        print(result)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    solve_recursive()
