def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def compress(start, end, n):
        tmp = arr[start][end]
        for i in range(start, start + n):
            for j in range(end, end + n):
                if tmp != arr[i][j]:
                    n //= 2
                    compress(start, end, n)
                    compress(start, end + n, n)
                    compress(start + n, end, n)
                    compress(start + n, end + n, n)
                    return
        answer[tmp] += 1

    compress(0, 0, n)

    return answer
