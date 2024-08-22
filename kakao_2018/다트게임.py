def solution(dartResult):
    score_cal = {}
    bonus_dic = {'S': 1, 'D': 2, 'T': 3}
    option_dic = {'*': 2, '#': -1}
    count = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i > 0 and dartResult[i-1].isdigit():
                score_cal[count] *= 10
            else:
                count += 1
                score_cal[count] = int(dartResult[i])
        if dartResult[i] in bonus_dic:
            score_cal[count] = score_cal[count] ** bonus_dic[dartResult[i]]
        if dartResult[i] in option_dic:
            if dartResult[i] == '*' and count-1 >= 1:
                score_cal[count-1] *= option_dic[dartResult[i]]
            score_cal[count] *= option_dic[dartResult[i]]

    return sum(score_cal.values())


dartResult = [
    # "1S2D*3T",
           "1D2S#10S",
            # "1D2S0T",
          # "1S*2T*3S",
          #    "1D#2S*3S",
              # "1T2D3D#",
              # "1D2S3T*"
]
for dart in dartResult:
    print(solution(dart))

