
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today,terms,privacies))
today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today,terms,privacies))
# today = "2020.12.28"
# terms = ["A 12", "B 1"]
# privacies = ["2019.01.01 A", "2020.11.28 B"]
# print(solution(today,terms,privacies))
# today = "2020.10.15"
# terms = ["A 100"]
# privacies = ["2018.06.16 A", "2008.02.15 A"]
# print(solution(today,terms,privacies))