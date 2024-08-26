def solution(s):
    answer = []
    s = s.split(" ")
    for st in s:
        if st != '' and st:
            answer.append(st.capitalize())
        else:
            answer.append(st)

    # print(s)
    return " ".join(answer)

s = " 3people unFollowed me  "
print(solution(s))
s = "for the last week"
print(solution(s))
s = "  for the what 1what  "
print(solution(s))
