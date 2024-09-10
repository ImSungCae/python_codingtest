a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

answer = 0
while True:
    if n > 100: break
    if a1 * n + a0 <= c * n:
        answer = 1
    else:
        answer = 0
        break
    n += 1


print(answer)