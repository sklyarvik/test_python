def add_atms(n, k, distances):
    # Проверка на коректность
    if n <= 0 or k < 0 or len(distances) != n - 1:
        return "Некорректные входные данные"

    # Сортировка расстояния в порядке убывания
    distances.sort(reverse=True)

    # Добавляет k банкоматов делая меньше максимальное расстояние
    for i in range(k):
        max_distance = distances.pop(0)
        new_distance = max_distance // 2
        distances.extend([new_distance, max_distance - new_distance])

    # Сортируем  по возрастанию
    distances.sort()

    return distances
n = 5
k = 3
distances = [100, 30, 20, 80]
result = add_atms(n, k, distances)
print(result)