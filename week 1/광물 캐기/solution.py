def solution(picks, minerals):
    answer = 0
    minerals = [list(minerals[i:i + 5]) for i in range(0, min(sum(picks) * 5, len(minerals)), 5)]
    costs = []  # 피로도 총합

    for mineral in minerals:
        cost = [0, 0, 0]
        for i in mineral:
            cost[0] += 1
            if i == "diamond":
                cost[1] += 5
            else:
                cost[1] += 1
            if i == "diamond":
                cost[2] += 25
            elif i == "iron":
                cost[2] += 5
            else:
                cost[2] += 1
        costs.append(cost)

    costs.sort(key=lambda x: (-x[2], -x[1]))

    for i in costs:
        if picks[0]:
            answer += i[0]
            picks[0] -= 1
        elif picks[1]:
            answer += i[1]
            picks[1] -= 1
        elif picks[2]:
            answer += i[2]
            picks[2] -= 1
        else:
            break

    return answer
