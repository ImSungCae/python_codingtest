x, y, w, h = map(int, input().split())

boundary = [0] * 4

boundary[0] = w - x
boundary[1] = h - y
boundary[2] = x
boundary[3] = y

print(min(boundary))