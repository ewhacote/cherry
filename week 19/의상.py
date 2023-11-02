from collections import defaultdict


def solution(clothes):
    dict = defaultdict(list)
    for cloth in clothes:
        dict[cloth[1]].append(cloth[0])
    answer = 1
    for i in dict:
        answer *= len(dict[i]) + 1
    answer -= 1
    return answer
