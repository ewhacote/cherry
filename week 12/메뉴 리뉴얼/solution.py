from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            com = combinations(sorted(order), c)
            tmp += com
        counter = Counter(tmp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(c) for c in counter if counter[c] == max(counter.values())]
    return sorted(answer)