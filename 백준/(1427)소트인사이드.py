import sys

N = sys.stdin.readline()

arr = [i for i in N]

del arr[len(arr) - 1]
# print(''.join(map(str,sorted(list(map(int,arr)), reverse=True))))

sys.stdout.write(''.join(map(str, sorted(arr, reverse=True))))