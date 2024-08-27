# def solution(A,B):
#     answer = 0
#     n = len(A)
#     A.sort()
#     B.sort(reverse = True)
#     for i in range(n):
#         answer += A[i]*B[i]
#
#     return answer
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
A = [1,2]
B = [3,4]
print(solution(A, B))
