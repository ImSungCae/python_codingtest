import sys

N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split()))

answer = [0] * M

# 문제 풀이 1 : dictionary 사용(이진 탐색을 사용하는 문제기때문에 적절하지 않음)
_dict = {}
for i in range(N):
    _dict[N_arr[i]] = 0

for j in range(M):
    if M_arr[j] in _dict:
        answer[j] = 1

# 문제 풀이 2 : 이진 탐색 (함수 x)
# N_arr.sort()

# for i in range(M):
#     low, high = 0, N-1
#     while low <= high:
#         mid = (low + high) // 2
#         if N_arr[mid] > M_arr[i]: # 중간 값보다 작다면
#             high = mid - 1 # 중간보다 왼쪽 한 칸 옆까지 탐색
#         elif N_arr[mid] < M_arr[i]: # 중간 값보다 크다면
#             low = mid + 1 # 중간보다 오른쪽 한 칸 옆까지 탐색
#         else:
#             answer[i] = 1
#             break

# 문제 풀이 2 : 이진 탐색 (재귀 함수 o)
# def binary_search(arr, target, low, high):
#     if low > high:
#         return 0
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return 1
#     elif arr[mid] > target:
#         return binary_search(arr, target, low, mid - 1)
#     else:
#         return binary_search(arr, target, mid + 1, high)
#
# for i in range(M):
#     answer[i] = binary_search(N_arr, M_arr[i], 0, N - 1)

sys.stdout.write(' '.join(map(str, answer)))



# # 재귀 함수로 구현한 이진 탐색
# def binary_search(arr, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#
#     # 원하는 값 찾은 경우 인덱스 변환
#     if arr[mid] == target:
#         return arr[mid]
#     # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
#     elif arr[mid] > target:
#         return binary_search(arr, target, start, mid - 1)
#     # 원하는 값이 중간점의 값보다 큰 경우 왼쪽 부분(절반의 오른쪽 부분) 확인
#     else:
#         return binary_search(arr, target, mid + 1, end)
#
#
#
#
# N = int(sys.stdin.readline())
# N_arr = list(map(int, sys.stdin.readline().split()))
# N_arr.sort()
#
# M = int(sys.stdin.readline())
# M_arr = list(map(int, sys.stdin.readline().split()))
# M_arr_sorted = sorted(M_arr)
#
#
# answer = [0] * M
#
# for i in N_arr:
#     result = binary_search(M_arr_sorted, i, 0, M - 1)
#     if result is not None:
#         answer[M_arr.index(result)] = 1
#
#
# sys.stdout.write(' '.join(map(str, answer)))