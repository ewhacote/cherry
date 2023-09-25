def solution(targets):
    e = 0
    targets.sort(key=lambda x: (x[1], x[0])) #e를 기준으로 오름차순 정렬 후 s를 기준으로 오름차순 정렬
    answer = 0

    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    return answer
