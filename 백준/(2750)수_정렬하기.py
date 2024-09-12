N = int(input())

arr = [int(input()) for _ in range(N)]

# sorted 사용
# for i in sorted(arr):
#     print(i)

# 버블정렬
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]

# 삽입정렬 1
# for i in range(1, N):
#     while i > 0 and arr[i] < arr[i - 1]:
#         arr[i], arr[i-1] = arr[i-1], arr[i]
#         i -= 1

# 삽입정렬 2
# for i in range(1, N):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = key

# 삽입정렬 2
# def insertion_sort(arr, left, right):
#     for i in range(left + 1, right + 1):
#         key = arr[i]
#         j = i - 1
#         while j >= left and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
# insertion_sort(arr, 0, N - 1)

for i in arr:
    print(i)

