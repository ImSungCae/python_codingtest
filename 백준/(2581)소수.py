M = int(input())
N = int(input())

output = []
for i in range(M,N+1):
    deci = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                deci += 1
                break

        if deci == 0:
            output.append(i)

try:
    print(f"{sum(output)}\n{min(output)}")
except ValueError:
    print(-1)