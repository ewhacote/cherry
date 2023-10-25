def solution(numbers):
    numbers.sort(reverse=True, key=lambda x: str(x) * 3)
    numbers = ''.join(str(s) for s in numbers)
    return "0" if numbers[0] == "0" else numbers
