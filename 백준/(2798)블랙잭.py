from itertools import permutations

n, m = map(int,input().split())
black_jack = list(map(int, input().split()))
max_sum_card = 0

for card in permutations(black_jack, 3):
    card_sum = sum(card)
    if max_sum_card < card_sum <= m:
        max_sum_card = card_sum

print(max_sum_card)