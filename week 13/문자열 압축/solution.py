def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):  # 쪼갤 수 있는 최대 길이가 문자열 s의 반 1..2..3..4 증가
        tmp = s[:i]
        cnt = 1  # 문자열이 연속으로 반복되는지 체크
        compressed = ''  # 압축된 문자열 저장
        for j in range(i, len(s), i):  # i 만큼 문자를 계속 쪼갬 ex) i=2 -> 2..4..6..8
            if tmp == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                compressed += str(cnt) + tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt == 1:
            cnt = ""
        compressed += str(cnt) + tmp

        result.append(len(compressed))
    return min(result)