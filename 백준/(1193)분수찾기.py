# 두 번째 답(정답)
# https://velog.io/@hwsa1004/%EB%B0%B1%EC%A4%80-1193%EB%B2%88-%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4
n = int(input())
line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a = n
    b = line - n + 1
elif line % 2 == 1:
    a = line - n + 1
    b = n

print(f'{a}/{b}')

# 첫 번째 답(틀림 : 시간초과)
# n = int(input())
#
# fountain = [1, 1]
# direct = 1
# x = 0
# j = 0
# z = 1
# for i in range(n):
#
#     if j == z:
#         direct *= -1
#         z += 1
#         j = 1
#         x += direct
#
#     if i > 0:
#         if j < z-1:
#             fountain[x+direct] -= 1
#         fountain[x] += 1
#
#     j += 1
# print('/'.join(map(str, fountain)))

