import sys

input = sys.stdin.readline

N = int(input())
points = []

# 점 좌표 입력
for i in range(1, N + 1):
    x, y = map(int, input().split())
    points.append((x, y))

# y좌표 기준으로 정렬, y좌표가 같을 경우 x좌표 기준으로 정렬
points.sort(key=lambda p: (p[1], p[0]))

# 정렬된 점 출력
for x, y in points:
    print(x, y)
