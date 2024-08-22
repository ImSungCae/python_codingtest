def solution(n, t, m, p):
    answer = ''
    tub = ''
    formatting = {2:'b', 8:'o',16:'X'}
    for i in range(t * m):
        j = format(i,formatting.get(n))
        tub += j
    for i in range(len(tub)):
        if i % m == (p-1) and len(answer) < t:
            answer += tub[i]

    return answer


n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))