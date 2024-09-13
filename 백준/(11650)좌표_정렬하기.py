import sys

# 빠른 입력 받기
input = sys.stdin.readline

# 첫 번째 줄에 점의 개수 N 입력
N = int(input())

# 좌표 리스트 입력 받기
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

# 좌표를 정렬
# x좌표를 기준으로 정렬하고, x좌표가 같으면 y좌표를 기준으로 정렬
coordinates.sort()

# 정렬된 좌표 출력
for x, y in coordinates:
    print(x, y)
