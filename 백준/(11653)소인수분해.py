import math


# 시간복잡도 최악의 경우 : O(n) / 일반적인 경우 : O(\sqrt{n})
n = int(input())
output = []
# i = 1
# while n != 1:
#     i += 1
#     if n % i == 0:
#         output.append(i)
#         n //= i
#         i = 1

for i in range(2, int(math.sqrt(n)) + 1):
    while n % i == 0:
        output.append(i)
        n //= i
if n > 1:
    output.append(n)

print('\n'.join(map(str, output)))