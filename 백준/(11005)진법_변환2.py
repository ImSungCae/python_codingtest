def solution(n, q):
    rev_base = ''
    conversion = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19 :'J', 20:'K', 21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}
    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            rev_base += conversion.get(mod)
        else:
            rev_base += str(mod)

    return rev_base[::-1]

i,j = input().split()
print(solution(int(i),int(j)))