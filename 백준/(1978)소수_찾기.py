N = int(input())
n = list(map(int, input().split()))

if N == len(n):
    answer = []
    for i in n:
        if i != 1:
            compare = []
            for j in range(1, i+1):
                if i % j == 0:
                    compare.append(j)

            if compare == [1, i]:
                answer.append(i)
    print(len(answer))
else:
    print("Error")