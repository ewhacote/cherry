from collections import deque


def solution(order):
    order = deque(order)
    main_line = deque(range(order[0], len(order) + 1))
    sub_line = list(range(1, order[0]))
    cnt = 0
    flag = True
    while flag and order:
        order_now = order.popleft()
        while True:
            if main_line and main_line[0] == order_now:
                main_line.popleft()
                cnt += 1
                break
            if sub_line and sub_line[-1] == order_now:
                sub_line.pop()
                cnt += 1
                break
            if not main_line:
                flag = False
                break
            else:
                sub_line.append(main_line.popleft())
    return cnt