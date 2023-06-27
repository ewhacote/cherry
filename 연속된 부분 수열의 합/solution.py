def solution(sequence, k):
    answer = []
    l = 0
    r = -1
    temp = 0
    while True:
        if temp < k:
            r+=1
            if r >= len(sequence):
                break
            temp += sequence[r]
        else:
            temp -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if temp == k:
            answer.append([l, r])
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]