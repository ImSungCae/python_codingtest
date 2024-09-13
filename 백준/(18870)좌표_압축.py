import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
arr = list(map(int, input().split()))

# 좌표 압축을 위한 정렬 및 중복 제거
arr2 = sorted(set(arr))

# 각 좌표에 대한 압축된 값 저장
dic = {arr2[i]: i for i in range(len(arr2))}

# 출력 성능 최적화
result = [str(dic[i]) for i in arr]
output(" ".join(result) + "\n")
