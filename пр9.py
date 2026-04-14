"""
Практическая работа 9, Вариант 4
Алгоритм Кнута-Морриса-Пратта для проверки перекрывающихся вхождений
"""


def compute_lps(pattern):
    """
    Вычисляет префикс-функцию (LPS - Longest Prefix Suffix) для образца.

    Args:
        pattern (str): Образец для поиска

    Returns:
        list: Массив LPS длиной len(pattern)
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Длина предыдущего наибольшего префикса-суффикса
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(pattern, text):
    """
    Поиск всех вхождений образца в текст с помощью алгоритма КМП.

    Args:
        pattern (str): Образец для поиска
        text (str): Текст, в котором выполняется поиск

    Returns:
        list: Список позиций (индексов) всех вхождений образца в текст
    """
    if not pattern or not text:
        return []

    m = len(pattern)
    n = len(text)

    # Вычисляем префикс-функцию
    lps = compute_lps(pattern)

    positions = []
    i = 0  # Индекс для текста
    j = 0  # Индекс для образца

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Найдено вхождение
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


def has_overlapping_occurrences(pattern, text):
    """
    Проверяет, есть ли перекрывающиеся вхождения образца в текст.
    Перекрывающиеся вхождения - когда расстояние между соседними
    вхождениями меньше длины образца.

    Args:
        pattern (str): Образец для поиска
        text (str): Текст, в котором выполняется поиск

    Returns:
        bool: True, если есть перекрывающиеся вхождения, иначе False

    Raises:
        ValueError: Если входные данные некорректны
    """
    # Плановая обработка ошибок
    if not isinstance(pattern, str) or not isinstance(text, str):
        raise ValueError("Образец и текст должны быть строками")

    if len(pattern) == 0:
        raise ValueError("Образец не может быть пустой строкой")

    if len(text) == 0:
        return False  # В пустом тексте нет вхождений

    # Находим все вхождения образца
    positions = kmp_search(pattern, text)

    # Если вхождений меньше 2, перекрываний быть не может
    if len(positions) < 2:
        return False

    m = len(pattern)

    # Проверяем расстояния между соседними вхождениями
    for i in range(len(positions) - 1):
        distance = positions[i + 1] - positions[i]
        if distance < m:
            return True

    return False


def main():
    """
    Основная функция для взаимодействия с пользователем.
    """
    print("Проверка перекрывающихся вхождений образца в текст")
    print("=" * 50)

    try:
        # Ввод данных
        pattern = input("Введите образец для поиска: ").strip()
        text = input("Введите текст: ").strip()

        # Проверка корректности ввода
        if not pattern:
            print("Ошибка: образец не может быть пустой строкой")
            return

        # Выполнение поиска и проверка перекрытий
        positions = kmp_search(pattern, text)
        has_overlap = has_overlapping_occurrences(pattern, text)

        # Вывод результатов
        print("\n" + "=" * 50)
        print(f"Образец: '{pattern}' (длина: {len(pattern)})")
        print(f"Текст: '{text}' (длина: {len(text)})")
        print(f"Найдено вхождений: {len(positions)}")

        if positions:
            print(f"Позиции вхождений: {positions}")

            # Вывод информации о расстояниях
            if len(positions) > 1:
                print("\nРасстояния между вхождениями:")
                for i in range(len(positions) - 1):
                    distance = positions[i + 1] - positions[i]
                    print(f"  Между позициями {positions[i]} и {positions[i + 1]}: {distance}")

            print(f"\nЕсть перекрывающиеся вхождения: {'ДА' if has_overlap else 'НЕТ'}")
        else:
            print("Вхождений не найдено")
            print("Есть перекрывающиеся вхождения: НЕТ")

    except ValueError as e:
        print(f"Ошибка входных данных: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    main()