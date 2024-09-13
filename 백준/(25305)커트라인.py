import sys

N, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr, reverse=True)
print(arr[k-1])