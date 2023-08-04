def solution(topping):
    answer = 0

    forward = set()
    backward = {}
    for i in topping:
        backward[str(i)] = backward.get(str(i), 0)
        backward[str(i)] += 1
    for i in topping:
        forward.add(i)
        backward[str(i)] -= 1
        if backward[str(i)] == 0:
            del backward[str(i)]
        if len(forward) == len(backward.keys()):
            answer += 1
    return answer