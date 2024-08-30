output = []
x = []
while True:
    n = int(input())

    if n == -1: break

    x.append(n)

    y = []
    for i in range(1, n):

        if n % i == 0: y.append(i)

    output.append(y)

for i in range(len(x)):
    if x[i] == sum(output[i]): print(str(x[i]) + " = " + (' + '.join(map(str, output[i]))))
    else: print(f"{x[i]} is NOT perfect.")
