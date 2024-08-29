n = int(input())

i = 1
j = 1
while j < n:
    j += 6*i
    i += 1

print(i)

# 처음 답 (틀림)
# n = int(input())
#
# i = 0
# j = 1
# x = 1
# while True:
#     i += 1
#     if n < j and n >= x or n == 1:
#         break
#     x = j+1
#     j += 6*i
#
# print(i)