# 첫 번째 답 (틀림 : 시간초과)
# A, B, V = map(int,input().split())
#
# snail = 0
# answer = 0
# if 1 <= B <= A <= V <= 1000000000:
#     while snail < V:
#         answer += 1
#         snail += A
#         if snail >= V:
#             break
#         snail -= B
#
# else:
#     print("Error")
#
# print(answer)
import math

# 두 번째 답 (정답) / 이해 안됨
A, B, V = map(int,input().split())
day = (V-B) / (A-B)
print(math.ceil(day))

