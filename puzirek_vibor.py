import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    """
    Сортировка пузырьком.
    Принимает список и возвращает отсортированный список.
    """
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break
    return sorted_arr

def selection_sort(arr):
    """
    Сортировка выбором.
    Принимает список и возвращает отсортированный список.
    """
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr

def insertion_sort(arr):
    """
    Сортировка вставками.
    Принимает список и возвращает отсортированный список.
    """
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(1, n):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr

def test_sorting_algorithms():
    """
    Тестирует время выполнения трёх алгоритмов сортировки
    и строит график зависимости времени от размера списка.
    """
    sizes = [100, 200, 500, 1000, 2000]
    bubble_times = []
    selection_times = []
    insertion_times = []

    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]

        # Тестируем сортировку пузырьком
        start_time = time.time()
        bubble_sort(test_data)
        bubble_times.append(time.time() - start_time)

        # Тестируем сортировку выбором
        start_time = time.time()
        selection_sort(test_data)
        selection_times.append(time.time() - start_time)

        # Тестируем сортировку вставками
        start_time = time.time()
        insertion_sort(test_data)
        insertion_times.append(time.time() - start_time)

    # Строим график
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, label='Пузырьком', marker='o')
    plt.plot(sizes, selection_times, label='Выбором', marker='s')
    plt.plot(sizes, insertion_times, label='Вставками', marker='^')

    plt.xlabel('Размер списка')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени выполнения алгоритмов сортировки')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Выводим результаты в табличном виде
    print("Результаты тестирования:")
    print(f"{'Размер':<8} {'Пузырьком':<12} {'Выбором':<12} {'Вставками':<12}")
    print("-" * 45)
    for i, size in enumerate(sizes):
        print(f"{size:<8} {bubble_times[i]:<12.6f} {selection_times[i]:<12.6f} {insertion_times[i]:<12.6f}")

# Запускаем тестирование
test_sorting_algorithms()
