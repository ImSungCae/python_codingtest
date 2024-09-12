def solution(numbers, hand):
    answer = ''
    hand_positon = ['*','#']
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            hand_positon[0] = number
        elif number in [3,6,9]:
            answer += 'R'
            hand_positon[1] = number
        else:
            hand_distance = [0, 0]
            number_idx= find_idx(number)
            left_idx = find_idx(hand_positon[0])
            right_idx = find_idx(hand_positon[1])
            
            hand_distance[0] = abs(number_idx[0][0] - left_idx[0][0]) + abs(number_idx[0][1] - left_idx[0][1])
            hand_distance[1] = abs(number_idx[0][0] - right_idx[0][0]) + abs(number_idx[0][1] - right_idx[0][1])
            
            if hand_distance[0] < hand_distance[1]:
                answer += 'L'
                hand_positon[0] = number
            elif hand_distance[0] > hand_distance[1]:
                answer += 'R'
                hand_positon[1] = number
            elif hand == 'left':
                answer += 'L'
                hand_positon[0] = number
            else:
                answer += 'R'
                hand_positon[1] = number
                
    return answer

def find_idx(num):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    return [(i,j) for i in range(len(keypad)) for j in range(len(keypad[i])) if keypad[i][j] == num]


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))