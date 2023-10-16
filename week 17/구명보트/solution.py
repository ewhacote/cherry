from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque()

    for i in people:
        queue.append(i)

    init = 0
    while len(queue) > 1 :
        if queue[init] + queue[-1] > limit:
            answer += 1
            queue.pop()
        else:
            queue.pop()
            queue.popleft()
            answer += 1

    if len(queue) == 1:
        queue.pop()
        answer += 1
    return answer