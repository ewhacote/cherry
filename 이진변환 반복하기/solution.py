def solution(s):
    cnt = 0
    zero_cnt = 0
    while True:
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1
        if s == "1":
            break
    return [cnt, zero_cnt]
