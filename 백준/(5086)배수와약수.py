output = []
while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        print('\n'.join(output))
        break

    if x % y == x:
        output.append("factor")
    elif x % y == 0:
        output.append("multiple")
    else:
        output.append("neither")


