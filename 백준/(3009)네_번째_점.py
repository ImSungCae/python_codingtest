first_dot = list(map(int, input().split()))
second_dot = list(map(int, input().split()))
third_dot = list(map(int, input().split()))

answer = [0, 0]
if first_dot[0] != second_dot[0] and first_dot[1] != second_dot[1]:
    answer[0] = (first_dot[0] + second_dot[0]) - third_dot[0]
    answer[1] = (first_dot[1] + second_dot[1]) - third_dot[1]
elif second_dot[0] != third_dot[0] and second_dot[1] != third_dot[1]:
    answer[0] = (second_dot[0] + third_dot[0]) - first_dot[0]
    answer[1] = (second_dot[1] + third_dot[1]) - first_dot[1]
else:
    answer[0] = (first_dot[0] + third_dot[0]) - second_dot[0]
    answer[1] = (first_dot[1] + third_dot[1]) - second_dot[1]

print(' '.join(map(str,answer)))