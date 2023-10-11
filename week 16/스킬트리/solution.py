def solution(skill, skill_trees):
    answer = 0
    sd = {k:v for v, k in enumerate(skill)}

    for skill_tree in skill_trees:
        status = [False] * (len(skill)+1)
        answer_flag = True
        for ch in skill_tree:
            if ch in skill:
                for idx in range(sd[ch]):
                    if not status[idx]:
                        answer_flag = False
                status[sd[ch]] = True

        if answer_flag:
            answer += 1
    return answer
