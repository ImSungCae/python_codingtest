import sys


# 첫 번째 풀이 - 시간 복잡도 O(n^2)
# def solution(prices):
    # max_profit = 0
    # for i in range(len(prices) - 1):
    #     for j in range(1, len(prices)):
    #         if prices[j] - prices[i] < 0:
    #             continue
    #         if prices[j] - prices[i] > max_profit:
    #             max_profit = prices[j] - prices[i]
    #
    # return max_profit

# 두 번째 풀이 - 시간 복잡도 O(n)
def solution(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price

    return max_profit

prices = list(map(int, sys.stdin.readline().split()))
print(solution(prices))





