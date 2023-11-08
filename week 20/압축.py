def solution(msg):
    dict = {}

    for num in range(0, 26):
        alpha = chr(num + 65)
        dict[alpha] = num + 1

    answer = [0]
    value = 26
    base = ""

    for i in range(len(msg)):
        base += msg[i]
        if not base in dict:
            value += 1
            dict[base] = value

            base = msg[i]
            answer.append(dict[base])
        else:
            answer[-1] = dict[base]
    return answer
