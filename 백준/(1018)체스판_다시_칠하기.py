N, M = map(int, input().split())

chess = [input() for _ in range(N)]

count = []

for a in range(N - 7):
    for b in range(M - 7): # 8 X 8로 자르기 위해, -7해준다.
        w_index = 0 # 흰색으로 시작
        b_index = 0 # 검정으로 시작
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0: # 짝수인 경우
                    if chess[i][j] != 'W': # W가 아니면, 즉 B인 경우
                        w_index += 1 # W로 칠하는 갯수
                    else: # W일때
                        b_index += 1 # B로 칠하는 갯수
                else: # 홀수인 경우
                    if chess[i][j] != 'W': # W가 아니면, 즉 B인 경우
                        b_index += 1 # B로 칠하는 갯수
                    else:
                        w_index += 1 # W로 칠하는 갯수
        count.append(w_index) # W로 시작할 때 경우의 수
        count.append(b_index) # B로 시작할 때 경우의 수

print(min(count))
