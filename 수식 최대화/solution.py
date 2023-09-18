from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    ops = ["+", "*", "-"]

    li = []
    s = 0
    for i, z in enumerate(expression):
        if z in ["+", "*", "-"]:
            li.append(expression[s:i])
            li.append(z)
            s = i + 1
    else:
        li.append(expression[s:])

    for op in ops:
        if op not in expression:
            ops.remove(op)
    primarity = permutations(ops)

    for case in primarity:
        stacks = [deque(li), deque()]
        t1 = 0
        for c in case:
            t1 = (t1 + 1) % 2
            t2 = (t1 + 1) % 2
            while len(stacks[t1]):
                items = stacks[t1].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == c:
                    c = stacks[t2].pop()
                    n = stacks[t2].pop()
                    items = str(eval(str(n) + c + str(items)))
                stacks[t2].append(items)
    return answer


solution("100-200*300-500+20")
