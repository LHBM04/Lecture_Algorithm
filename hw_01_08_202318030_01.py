"""실습 과제 1: O(n^2) 기초 정렬 알고리즘 3개를 구현한다."""

def bubble_sort(array: list[int]):
    """인접한 두 원소를 비교하며 큰 값을 오른쪽으로 보낸다."""
    n: int = len(array)

    for i in range(n):
        for j in range(i, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def selection_sort(array: list[int]):
    """정렬되지 않은 구간의 최솟값을 찾아 왼쪽에 놓는다."""
    n: int = len(array)

    for i in range(n):
        min_at: int = i

        for j in range(i + 1, n):
            if array[j] < array[min_at]:
                min_at = j

        array[i], array[min_at] = array[min_at], array[i]

def insertion_sort(array: list[int]):
    """왼쪽의 정렬된 구간에 다음 원소를 알맞은 위치로 삽입한다."""
    n: int = len(array)

    for i in range(1, n):
        current_value: int = array[i] # 주인공이 될 값을 미리 빼둔다.
        current_at: int = i

        for j in range(i - 1, -1, -1):
            if array[j] <= current_value: # 값이 작으면 그 앞은 이미 정렬이 된 부분임. 스킵해야 함.
                break

            array[current_at] = array[j] # 옮길 값들을 한 칸씩 뒤로 밀어낸다.
            current_at -= 1

        array[current_at] = current_value # 최종적으로 위치해야 할 자리에 주인공을 넣는다.

if __name__ == "__main__":
    data: list[int] = [17, 12, 10, 30, 22, 29, 20, 11, 30, 28, 26, 30]

    bubble_data: list[int] = list(data)
    print("Bubble Sort")
    print("정렬 전:", bubble_data)
    bubble_sort(bubble_data)
    print("정렬 후:", bubble_data)
    print()

    selection_data: list[int] = list(data)
    print("Selection Sort")
    print("정렬 전:", selection_data)
    selection_sort(selection_data)
    print("정렬 후:", selection_data)
    print()

    insertion_data: list[int] = list(data)
    print("Insertion Sort")
    print("정렬 전:", insertion_data)
    insertion_sort(insertion_data)
    print("정렬 후:", insertion_data)
