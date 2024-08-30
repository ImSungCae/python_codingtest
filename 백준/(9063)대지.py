# 세 번째 시도
import sys

n = int(sys.stdin.readline().strip())
dot = [[], []]
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    dot[0].append(x)
    dot[1].append(y)

print((max(dot[0]) - min(dot[0])) * (max(dot[1]) - min(dot[1])))

# 두 번째 시도 (max(), min()을 쓰지않고 한번 순회할때 최솟값 최댓값 구하기 / 맞긴한데 첫번째 시도와 동일하게 속도측면에서 이득이 미미함)
# n = int(input())
# max_x = -10000
# min_x = 10000
# max_y = -10000
# min_y = 10000
# for _ in range(n):
#     x, y = (map(int, input().split()))
#     if max_x < x:
#         max_x = x
#     if min_x > x:
#         min_x = x
#     if max_y < y:
#         max_y = y
#     if min_y > y:
#         min_y = y
#
# print((max_x - min_x) * (max_y - min_y))
# 첫 번째 시도 (맞는데 시간이 오래 걸림)
# n = int(input())
# dot = [[], []]
# for _ in range(n):
#     x, y = (map(int, input().split()))
#     dot[0].append(x)
#     dot[1].append(y)
#
# print((max(dot[0]) - min(dot[0])) * (max(dot[1]) - min(dot[1])))
