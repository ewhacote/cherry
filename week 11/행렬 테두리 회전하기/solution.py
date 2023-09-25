def solution(rows, columns, queries):
    array = []
    for i in range(rows):
        array.append([rows * i + j for j in range(1, columns + 1)])

    answer = []
    for query in queries:
        query = [x - 1 for x in query]
        tmp = array[query[0]][query[1]]
        small = tmp

        # left
        for i in range(query[0] + 1, query[2] + 1):
            array[i - 1][query[1]] = array[i][query[1]]
            small = min(small, array[i][query[1]])
        # bottom
        for i in range(query[1] + 1, query[3] + 1):
            array[query[2]][i - 1] = array[query[2]][i]
            small = min(small, array[query[2]][i])
        # right
        for i in range(query[2] - 1, query[0] - 1, -1):
            array[i + 1][query[3]] = array[i][query[3]]
            small = min(small, array[i][query[3]])
        # top
        for i in range(query[3] - 1, query[1] - 1, -1):
            array[query[0]][i + 1] = array[query[0]][i]
            small = min(small, array[query[0]][i])
        array[query[0]][query[1] + 1] = tmp

        answer.append(small)

    return answer