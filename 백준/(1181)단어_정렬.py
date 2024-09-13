import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().strip())
arr = list(set(arr))
arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)

