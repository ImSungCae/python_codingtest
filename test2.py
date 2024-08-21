# https://school.programmers.co.kr/learn/courses/30/lessons/150370

import datetime as dt

def solution(today, terms, privacies):
    answer = []
    term_list = []
    privacies_list = []
    destruction_list = []
    for term in terms:
        term_list.append(term.split(' '))
        
    for privice in privacies:
        privacies_list.append(privice.split(' '))
        
    for i in range(len(privacies)):
        for j in range(len(term_list)):
            if privacies_list[i][1] == term_list[j][0]:
                date = privacies_list[i][0].split('.')
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])
                
                day -= 1
                
                if day == 0:
                    day = 28
                    month -= 1
                    if month == 0:
                        month = 12
                        year -= 1
                
                month += int(term_list[j][1])
                
                if month > 12:
                    if month % 12 == 0: year += int(month / 12) - 1
                    else: year += int(month / 12)
                    month -= 12 * int(month / 12)
                    if month == 0:
                        month = 12
                    
                if len(str(month)) <= 1:
                    month = '0' + str(month)
                if len(str(day)) <= 1:
                    day = '0' + str(day)
                destruction_list.append(str(year) + '.' + str(month) + '.' + str(day))
                
                
                
        if today > destruction_list[i]:
            answer.append(i+1)
                
    return answer

# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# print(solution(today,terms,privacies))
# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# print(solution(today,terms,privacies))
today = "2020.12.28"
terms = ["A 12", "B 1"]
privacies = ["2019.01.01 A", "2020.11.28 B"]
print(solution(today,terms,privacies))
# today = "2020.10.15"
# terms = ["A 100"]
# privacies = ["2018.06.16 A", "2008.02.15 A"]
# print(solution(today,terms,privacies))