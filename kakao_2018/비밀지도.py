def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(format(arr1[i]|arr2[i],'b').rjust(n,'0'))
        answer[i] = str(answer[i]).replace('1', '#')
        answer[i] = str(answer[i]).replace('0', ' ')
        
    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n,arr1,arr2))