def solution(s):
    answer = ''
    count = {}
    for st in s.upper():
        if st in count:
            count[st] += 1
        else: count[st] = 1

    t = [k for k,v in count.items() if max(count.values()) == v]

    if len(t) > 1:
        answer = '?'
    else:
        answer = ''.join(t)

    return answer

s = input()
print(solution(s))