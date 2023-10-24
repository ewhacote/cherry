def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] > answer:
            answer = i+1
        else:
            break
    return answer