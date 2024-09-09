# def solution(input):
#     max_profit = 0
#     for i in range(len(input) - 1):
#         for j in range(1, len(input)):
#             if input[j] - input[i] < 0:
#                 continue
#             elif input[j] - input[i] > max_profit:
#                 max_profit = input[j] - input[i]
#
#     return max_profit

def solution(input):
    min_price = input[0]
    max_profit = 0

    for price in input[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price

    return max_profit


# input = [7, 1, 3, 4, 6]
input = [7, 6, 5]
print(solution(input))