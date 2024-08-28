s = int(input())
cal = [int(input()) for _ in range(s)]
dollor = [25,10,5,1]
for c in cal:
    out = []
    for dol in dollor:
        n, mod = divmod(c, dol)
        out.append(n)
        c = mod
    print(' '.join(map(str,out)))
        

