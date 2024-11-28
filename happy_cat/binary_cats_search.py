def can_place_cats(n, beds, occupied, min_distance, k):
    # Эта функция проверяет, можем ли мы расставить котиков так,
    # чтобы минимальное счастье было не меньше min_distance.
    
    if k == 0:
        # Если нет занятых котиками лежанок, то просто расставляем котиков на свободных
        placed = 0
        last_position = -float('inf')
        
        for bed in beds:
            if bed - last_position >= min_distance:
                placed += 1
                last_position = bed
                if placed == n:
                    return True
        return placed >= n
    
    else:
        # Если есть занятые лежанки, то первый котик должен сидеть на одной из занятых
        placed = 1  # Один котик уже на занятой лежанке
        last_position = occupied[0]  # Начинаем с координаты первой занятой лежанки

        # Ищем подходящие места для остальных котиков
        for bed in beds:
            if bed in occupied:
                continue  # Пропускаем уже занятые лежанки
            # Проверяем, можем ли мы поставить котика на эту лежанку
            if abs(bed - last_position) >= min_distance:
                placed += 1
                last_position = bed
                if placed == n:
                    return True
        return placed >= n


def solve(n, m, k, beds, occupied):
    # Сортируем координаты всех лежанок (включая занятые и свободные)
    beds.sort()
    occupied.sort()

    # Бинарный поиск по минимальному возможному счастью
    left, right = 0, beds[-1] - beds[0]  # Максимальное расстояние между самой левой и правой лежанкой
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_cats(n, beds, occupied, mid, k):  # Передаем k как параметр
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Обработка ввода данных
def main():
    try:
        # Чтение данных из ввода
        n, m, k = map(int, input().split())  # количество котиков, лежанок и занятых
        beds = list(map(int, input().split()))  # координаты всех лежанок
        if k > 0:
            occupied = list(map(int, input().split()))  # координаты занятых лежанок
        else:
            occupied = []

        # Вызов основной функции
        result = solve(n, m, k, beds, occupied)

        # Вывод результата
        print(result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    main()
