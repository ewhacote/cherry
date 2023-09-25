def solution(plans):
    answer = []
    stop = []
    plans.sort(key=lambda x: x[1])
    for p in plans:
        p[1], p[2] = int(p[1][:2]) * 60 + int(p[1][3:]), int(p[2])

    while plans:
        if len(plans) > 1:
            t1 = plans[0][1] + plans[0][2]
            t2 = plans[1][1]
            if t1 > t2:
                stop.append([t1 - t2, plans[0][0]])
                plans.pop(0)
            else:
                answer.append(plans[0][0])
                plans.pop(0)
                time = t2 - t1
                while stop:
                    if stop[-1][0] <= time:
                        time -= stop[-1][0]
                        answer.append(stop.pop()[1])
                    else:
                        stop[-1][0] -= time
                        break
        else:
            answer.append(plans.pop(0)[0])

    for s in stop[::-1]:
        answer.append(s[1])
    return answer
