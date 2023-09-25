def solution(numbers):
    answer = []
    for i in numbers:
        num = i
        count = 0
        while i % 2 == 1:
            count += 1
            i //= 2
        answer.append(num + 2 ** (count - 1) if count else num + 1)

    return answer