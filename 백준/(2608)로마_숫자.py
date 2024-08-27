def romeNumber(s):
    answer = [0,'']
    rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rome_reverse = {v:k for k,v in rome.items()}
    s_sum = [0] * len(s)

    for i in range(len(s)):
        for j in range(len(s[i])):
            if j > 0 and rome.get(s[i][j-1]) < rome.get(s[i][j]) :
                s_sum[i] += abs(rome.get(s[i][j]) - rome.get(s[i][j-1]) * 2)
            else: s_sum[i] += rome.get(s[i][j])

    answer[0] = sum(s_sum)
    for key in reversed(list(rome.keys())):
        if int(answer[0] / rome.get(key)) in [4,9] or str(answer[0])[0] == '9':
            repeat = int(answer[0] / rome.get(key))
            if str(answer[0])[0] == '9' and repeat not in [4,9]: continue
            else:
                answer[1] += rome_reverse.get(rome.get(key)) + (rome_reverse.get(rome.get(key) * (repeat+1)))
        else:
            answer[1] += rome_reverse.get(rome.get(key)) * int(answer[0] / rome.get(key))
        answer[0] %= rome.get(key)


    return str(sum(s_sum)) + "\n" + answer[1]
    # return "\n".join(map(str, answer))

# s = []
# s.append(input())
# s.append(input())
s = [input() for _ in range(2)]
print(romeNumber(s))