def solution(p):
    # 1
    if p == '':
        return p
    # 2
    u, v = divide(p)
    # 3
    if check(u):
        return u + solution(v)
    # 4
    else:
        temp = '(' + solution(v) + ')'
        for x in u[1:-1]:
            if x == '(':
                temp += ')'
            else:
                temp += '('
        return temp


def divide(p):
    left, right = 0, 0
    for k in range(len(p)):
        if p[k] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:k + 1], p[k + 1:]


def check(u):
    q = []
    for x in u:
        if not q:
            q.append(x)
        else:
            if x == ')' and q[-1] == '(':
                q.pop()
            else:
                q.append(x)
    if q:
        return False
    return True
