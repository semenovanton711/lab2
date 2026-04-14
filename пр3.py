try:
    n = int(input())
    if n < 1:
        print("Ошибка: количество часов должно быть не менее 1")
        exit()
    passengers = list(map(int, input().split()))
    if len(passengers) != n:
        print(f"Ошибка: ожидалось {n} чисел, получено {len(passengers)}")
        exit()
    for p in passengers:
        if p < 0:
            print("Ошибка: количество пассажиров не может быть отрицательным")
            exit()
    k = int(input())
    if k < 1 or k > n:
        print(f"Ошибка: продолжительность часа пик должна быть от 1 до {n}")
        exit()
    max_sum = 0
    for i in range(n - k + 1):
        current_sum = sum(passengers[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)
except ValueError:
    print("Ошибка: введены некорректные данные (ожидались целые числа)")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")