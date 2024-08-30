import sys

answer = []
while True:
    n = sorted(list(map(int, sys.stdin.readline().split())))

    if n[0] == n[1] == n[2] == 0:
        break
    if n[2] < n[0] + n[1] :
        if n[0] == n[1] == n[2]:
            answer.append("Equilateral")
        elif n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
            answer.append("Isosceles")
        else:
            answer.append("Scalene")
    else:
        answer.append("Invalid")

print('\n'.join(map(str, answer)))