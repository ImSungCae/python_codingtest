import sys

# 빠른 입력 받기
input = sys.stdin.readline

# 첫 번째 줄에 수의 개수 N 입력
N = int(input())

# 배열 입력 받기
arr = [int(input()) for _ in range(N)]

# Timsort를 사용한 기본 정렬
arr.sort()

# 빠른 출력
sys.stdout.write('\n'.join(map(str, arr)) + '\n')
