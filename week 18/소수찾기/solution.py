from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(map(str, numbers))
    candits = set()

    for i in range(1, len(numbers)+1):
        permute = list(permutations(numbers, i))
        permute = set(list(map(lambda x: int(''.join(x)), permute)))
        candits = candits.union(permute)
    candits = list(filter(lambda x: x > 1, list(candits)))


    for num in list(candits):
        flag = True
        for i in range(2, num//2+1):
            if not flag:
                break
            if num % i == 0:
                flag = False
        if flag:
            answer += 1

    return answer