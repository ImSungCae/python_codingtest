p, q = map(int, input().split())
K = []

for i in range(1, p+1):
    if p % i == 0:
        K.append(i)

    if len(K) == q:
        print(K[q-1])
        break

if len(K) < q: print(0)