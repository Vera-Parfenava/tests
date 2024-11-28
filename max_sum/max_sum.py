def max_game_result(n, piles):
    """
    Вычисляет максимальный результат игры между Эмси и Райдом за линейное время O(n).
    """
    # Найти минимальное и максимальное значения
    min_value = min(piles)
    max_value = max(piles)

    # Найти первый и последний индексы минимального значения
    first_min_index = -1
    last_min_index = -1
    first_max_index = -1
    last_max_index = -1

    for i in range(n):
        if piles[i] == min_value:
            if first_min_index == -1:
                first_min_index = i
            last_min_index = i
        if piles[i] == max_value:
            if first_max_index == -1:
                first_max_index = i
            last_max_index = i

    # Возможные отрезки для выбора
    ranges = [
        (first_min_index, first_max_index),
        (first_min_index, last_max_index),
        (last_min_index, first_max_index),
        (last_min_index, last_max_index),
    ]

    # Найти максимальную сумму для всех возможных отрезков
    max_result = 0
    for start, end in ranges:
        start, end = min(start, end), max(start, end)
        current_sum = sum(piles[start:end + 1])
        max_result = max(max_result, current_sum)

    return max_result


if __name__ == "__main__":
    try:
        # Ввод количества кучек
        n = int(input())
        if n < 1:
            raise ValueError("Количество кучек должно быть положительным числом.")

        # Ввод количества камней в кучках
        piles = list(map(int, input().split()))
        if len(piles) != n:
            raise ValueError("Количество введенных значений не совпадает с числом кучек.")

        if any(pile <= 0 for pile in piles):
            raise ValueError("Количество камней в каждой кучке должно быть положительным числом.")

        # Вычисление и вывод результата
        result = max_game_result(n, piles)
        print(result)
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")