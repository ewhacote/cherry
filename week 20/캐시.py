from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    for i in cities:
        i = i.lower()
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer += 1
        else:
            cache.append(i)
            answer += 5
    return answer