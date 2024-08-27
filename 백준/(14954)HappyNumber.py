def happyNumber(s):
    # answer = ''
    happy = s
    while True:
        sum_happy = 0
        for st in happy:
            sum_happy += int(st) ** 2

        happy = str(sum_happy)

        if happy == '4':
            answer = 'UNHAPPY'
            break
        elif happy == '1':
            answer = 'HAPPY'
            break

    return answer

s = input()
print(happyNumber(s))