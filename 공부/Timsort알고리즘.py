MIN_RUN = 32

# 삽입 정렬
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 병합 함수
def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    l = r = 0
    k = left

    while l < len(left_part) and r < len(right_part):
        if left_part[l] <= right_part[r]:
            arr[k] = left_part[l]
            l += 1
        else:
            arr[k] = right_part[r]
            r += 1
        k += 1

    # 남은 원소들 복사
    while l < len(left_part):
        arr[k] = left_part[l]
        l += 1
        k += 1

    while r < len(right_part):
        arr[k] = right_part[r]
        r += 1
        k += 1

# Timsort 구현
def timsort(arr):
    n = len(arr)

    # 배열을 run 크기 단위로 나누어 삽입 정렬 수행
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min(i + MIN_RUN - 1, n - 1))

    # 작은 run들을 병합
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), n - 1)

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# # 테스트
# arr = [5, 21, 7, 23, 19, 20, 3, 8, 15, 1, 9, 6, 13, 2]
# print("정렬 전:", arr)
# timsort(arr)
# print("정렬 후:", arr)

N = int(input())

arr = [int(input()) for _ in range(N)]

# for i in sorted(arr):
#     print(i)

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
timsort(arr)
for i in arr:
    print(i)