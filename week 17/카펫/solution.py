def solution(brown, yellow):
    total = brown + yellow
    check = []
    h = 0
    v = 0
    for i in range(3, total + 1):
        if total % i == 0:
            check.append(i)

    for c in check:
        v = c
        h = int(total / v)
        if (v - 2) * (h - 2) == yellow:
            return [h, v]
