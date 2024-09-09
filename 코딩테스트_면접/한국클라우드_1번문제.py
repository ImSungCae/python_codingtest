import sys

def solution(n):
    count = 0
    while n != 0:
        if n % 2 == 0: # 짝수
            n /= 2
            count += 1
        elif n % 2 == 1: # 홀수
            n -= 1
            count += 1

    return count

n = int(sys.stdin.readline())
print(solution(n))
