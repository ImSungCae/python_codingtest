# def solution(s): # 스택/큐를 사용하지 않은 버전
#     count_s = 0
#     for st in s:
#         if count_s < 0: return False
#         else:
#             if st == '(': count_s += 1
#             if st == ')': count_s -= 1
#
#     if count_s == 0: return True
#     else: return False

def solution(s): # 스택/큐를 사용한 버전
    stack_s = []
    for st in s:
        if st == '(': stack_s.append(st)
        if st == ')':
            try:
                stack_s.pop()
            except IndexError:
                return False

    return len(stack_s) == 0

s = "()()"
print(solution(s))
s = "(())()"
print(solution(s))
s = ")()("
print(solution(s))
s = "(()("
print(solution(s))
s = "() )( ()"
print(solution(s))
