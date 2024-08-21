# https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    l = len(friends)
    answer = [0] * l
    
    # 사용 배열 초기화
    sended_gift = [0] * l
    received_gift = [0] * l
    gift_indices = [0] * l
    given_and_received = [[0 for j in range(l)] for i in range(l)]
    
    # 주고받은 선물 반복문
    for gift in gifts:
        
        # 공백을 기준으로 split
        split_gift = gift.split(" ")
        # 0번째는 선물 준 사람
        send_people = split_gift[0]
        # 1번째는 선물 받은 사람
        receive_people = split_gift[1]
        
        
        given_and_received[friends.index(send_people)][friends.index(receive_people)] += 1
        
        # 준 선물 / 받은 선물 카운트
        sended_gift[friends.index(send_people)] += 1
        received_gift[friends.index(receive_people)] += 1
        
    # 선물 지수 계산
    for i in range(l):
        gift_indices[i] = sended_gift[i] - received_gift[i]
        
    for i in range(l):
        for j in range(l):
            if given_and_received[i][j] > 0 and given_and_received[i][j] > given_and_received[j][i]:
                answer[i] += 1
            elif i != j and given_and_received[i][j] == given_and_received[j][i]:
                if gift_indices[i] > gift_indices[j]:
                    answer[i] += 1
    return max(answer)


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends,gifts))
# result : 2


