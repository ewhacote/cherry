def solution(k, ranges):
    answer = []
    s = [k]

    while True:
        if k == 1:
            break
        elif k % 2 == 0:
            k //= 2
            s.append(k)
        else:
            k *= 3
            k += 1
            s.append(k)

    sl = []

    for i in range(1, len(s)):
        sl.append((s[i - 1] + s[i]) / 2)

    for i in ranges:
        x = i[0]
        y = len(sl) + i[1]

        if x == y:
            answer.append(0.0)
        elif x > y:
            answer.append(-1.0)
        else:
            answer.append(sum(sl[x:y]))
    return answer