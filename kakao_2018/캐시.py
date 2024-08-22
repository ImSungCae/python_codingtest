def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [i.lower() for i in cities]
    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
    return answer

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))




# def solution(cacheSize, cities):
#     cities = [c.lower() for c in cities]
#     cache=[]
#     answer=0
#
#     if cacheSize==0:
#         return len(cities) * 5
#     else:
#         for i in cities:
#             if not i in cache:
#                 if cacheSize>len(cache):
#                     cache.append(i)
#                     answer+=5
#                 else:
#                     cache.pop(0)
#                     cache.append(i)
#                     answer+=5
#             else:
#                 cache.pop(cache.index(i))
#                 cache.append(i)
#                 answer+=1
#
#     return answer