def solution(s):
    answer = []

    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    for i in s:
        tmp = i.split(",")
        for t in tmp:
            if int(t) not in answer:
                answer.append(int(t))
    return answer