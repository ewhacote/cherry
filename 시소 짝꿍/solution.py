def solution(weights):
    dict = {}
    answer = 0
    for w in weights:
        dict[w] = dict.get(w, 0) + 1

    for w in weights:
        if w % 2 == 0: answer += dict.get(w * 3 // 2, 0)
        if w % 3 == 0: answer += dict.get(w * 4 // 3, 0)
        answer += dict.get(w * 2, 0)
    for w in weights:
        dict[w] -= 1
        answer += dict[w]
    return answer
