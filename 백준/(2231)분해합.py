# 첫 번째 풀이 - 시간복잡도 O(N log N)
# n = int(input())
# x = n // 2
# m = 0
# while True:
#     n1 = list(map(int, str(x)))
#     m = x + sum(n1)
#     if x > n:
#         print(0)
#         break
#     if m == n:
#         print(x)
#         break
#     x += 1

# 두 번째 풀이 - 시간복잡도 O(log N^2)
n = int(input())

# 탐색 범위를 N에서 자리수 최대 합을 뺀 값부터 시작
start = max(1, n - 9 * len(str(n)))
print(start)
m = 0

for x in range(start, n):
    # x의 분해합 계산
    m = x + sum(map(int, str(x)))
    if m == n:
        print(x)
        break
else:
    print(0)