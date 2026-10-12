"""실습 과제 2: Heap Sort/Count Sort를 구현한다."""

def heapify(array: list[int], root: int, count: int) -> None:
    left: int = root * 2 + 1
    if left >= count:
        return

    right: int = root * 2 + 2
    largest: int = left
    if right < count:
        if array[right] > array[largest]:
            largest = right

    if array[largest] > array[root]:
        array[root], array[largest] = array[largest], array[root]
        heapify(array, largest, count)

def heap_sort(array: list[int]) -> None:
    count: int = len(array)

    if count > 1:
        for root in range(count // 2 - 1, -1, -1):
            heapify(array, root, count)

    for last in range(count - 1, 0, -1):
        array[0], array[last] = array[last], array[0]

        if last > 1:
            heapify(array, 0, last)

def count_sort(array: list[int]) -> None:
    counts: list[int] = [0] * (max(array) + 1)
    for index, value in enumerate(array):
        counts[value] += 1

    for right in range(1, len(counts)):
        left = right - 1
        counts[right] += counts[left]

    result: list[int | None] = [None] * len(array)
    
    for index in range(len(array) - 1, -1, -1):
        value: int = array[index]
        counts[value] -= 1
        at: int = counts[value]
        result[at] = value

    array[:] = result

if __name__ == '__main__':
    data: list[int] = [17, 12, 10, 30, 22, 29, 20, 11, 30, 28, 26, 30]

    heap_data: list[int] = list(data)
    print("Heap Sort")
    print("정렬 전:", heap_data)
    heap_sort(heap_data)
    print("정렬 후:", heap_data)
    print()

    count_data: list[int] = list(data)
    print("Count Sort")
    print("정렬 전:", count_data)
    count_sort(count_data)
    print("정렬 후:", count_data)
    print()