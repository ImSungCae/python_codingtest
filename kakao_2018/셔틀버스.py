# 9:00 부터 총 n회 t분 간격으로 역에 도착
# 하나의 셔틀에는 최대 m명
# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 최대 m, 크루가 대기열에 도착하는 시간 timetable
# 출력 : 셔틀을 탈 수 있는 제일 늦은 시간

# def solution(n, t, m, timetable):
#     answer = ''
#     hour = "09"
#     min = "00"
#     shuttle_bus = []
#     for i in range(n):
#         shuttle_bus.append(hour+":"+min)
#         min = int(min) + t
#         if min >= 60:
#             hour = int(hour) + int(min / 60)
#             min -= int(min / 60) * 60
#         if len(str(hour)) <= 1:
#             hour = '0' + str(hour)
#         else: hour = str(hour)
#
#         if len(str(min)) <= 1:
#             min = '0' + str(min)
#         else: min = str(min)
#
#     count = [0] * len(shuttle_bus)
#     for i in range(len(shuttle_bus)):
#         for crew in sorted(timetable):
#             if shuttle_bus[i] >= crew:
#                 count[i] += 1
#                 timetable.remove(crew)
#                 if count[i] >= m:
#                     sp = crew.split(':')
#                     sp_hour = sp[0]
#                     sp_min = sp[1]
#                     if sp_min == '00':
#                         sp_hour = str(int(sp_hour) - 1)
#                         sp_min = '59'
#                     else:
#                         sp_min = str(int(sp_min) - 1)
#                     if len(str(sp_hour)) <= 1:
#                         sp_hour = '0' + str(sp_hour)
#                     else: sp_hour = str(sp_hour)
#
#                     if len(str(sp_min)) <= 1:
#                         sp_min = '0' + str(sp_min)
#                     else: sp_min = str(sp_min)
#
#                     answer = sp_hour + ":" + sp_min
#                 else:
#                     answer = shuttle_bus[i]
#             elif count[i] < m:
#                 answer = shuttle_bus[i]
#
#
#
#     print(count)
#     print(shuttle_bus)
#     return answer
def solution(n, t, m, timetable):
    answer = 0
    # 버스 배차 간격
    ft = 60*9
    # timetable 분으로 전환
    bus = {ft+t*i:[] for i in range(n)}
    time_min = []
    for time in timetable:
        hour,minute = map(int, time.split(':'))
        time_min.append(hour*60+minute)
    # 정렬
    time_min.sort()
    get_in = [0] * len(time_min)
    for bs in bus:
        for st in range(len(time_min)):
            if time_min[st] <= bs and get_in[st] == 0 and len(bus[bs]) < m:
                bus[bs].append(time_min[st])
                get_in[st]=1
    print(bus)
    lk = list(bus.keys())[-1]
    if len(bus[lk]) < m: answer = lk
    else:
        if bus[lk][0] != bus[lk][-1]:
            answer = bus[lk][-1]-1
        else: answer = bus[lk][0]-1
    c_hour, c_min = str(answer//60).zfill(2), str(answer % 60).zfill(2)
    return c_hour+':'+c_min




n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))
n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
n = 1
t = 1
m = 1
timetable = ["23:59"]
print(solution(n, t, m, timetable))
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))
n = 3
t = 1
m = 2
timetable = ["06:00", "23:59", "05:48", "00:01", "00:01"]
print(solution(n, t, m, timetable)) # 09:02
n = 10
t = 25
m = 1
timetable = ["09:00", "09:10", "09:20", "09:30", "09:40", "09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]
print(solution(n, t, m, timetable)) # 10:29
n = 2
t = 10
m = 2
timetable = ["09:10", "09:10", "09:10"]
print(solution(n, t, m, timetable)) #"09:09"
n = 2
t = 5
m = 1
timetable = ["09:05", "09:05"]
print(solution(n, t, m, timetable)) # "09:04"
n = 1
t = 1
m = 1
timetable = ["09:00", "09:05"]
print(solution(n, t, m, timetable)) # "08:59"
n = 1
t = 1
m = 1
timetable = ["08:55"]
print(solution(n, t, m, timetable)) # "08:54"