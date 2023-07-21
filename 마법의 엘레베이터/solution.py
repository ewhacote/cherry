def solution(storey):
    digits = list(map(int, str(storey)))
    answer = storey
    stack = [[digits, 0]]
    while stack:
        curr_digits, curr_count = stack.pop()

        if not curr_digits:
            answer = min(answer, curr_count)
            continue

        curr_last_digit = curr_digits.pop()
        stack.append([curr_digits, curr_count + curr_last_digit])

        if curr_digits:
            post_digits = curr_digits.copy()
            post_digits[-1] += 1
            stack.append([post_digits, curr_count + (10 - curr_last_digit)])
        else:
            answer = min(answer, curr_count + (10 - curr_last_digit) + 1)

    return answer