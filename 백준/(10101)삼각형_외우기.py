import sys

n = [int(sys.stdin.readline().strip()) for i in range(3)]

if n[0] == n[1] == n[2] == 60:
    print("Equilateral")
elif sum(n) == 180:
    if n[0] == n[1]  or n[0] == n[2] or n[1] == n[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")