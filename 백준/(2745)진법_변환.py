# def solution(n, q):
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, q)
#         rev_base += str(mod)
#
#     return rev_base[::-1]
#
# i,j = input().split()
# print(solution(int(i, int(j)), 10))

i,j = input().split()
print(int(i, int(j)))