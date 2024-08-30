N = int(input())
compare = 0
index = 0
if 0 <= N <= 99:
    if compare == N: index += 1
    while compare != N:
        if index == 0: compare=N
        x, y = divmod(compare,10)
        compare = y*10+((x+y)%10)
        index += 1
    print(index)
else:
    print("Error")

