from collections import deque


def bfs(r, c, row, col, data):
    visited = [[float("inf")] * col for i in range(row)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    while q:
        x, y = q.popleft()
        fx, fy = x, y
        for i in range(4):
            count = 0
            x, y = fx, fy
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or nx == row or 0 > ny or ny == col or data[nx][ny] == 'D':
                    if data[x][y] == 'G':
                        return visited[fx][fy] + 1
                    if count > 0 and visited[fx][fy] + 1 < visited[x][y]:
                        q.append((x, y))
                        visited[x][y] = visited[fx][fy] + 1
                    break
                x, y = nx, ny
                count += 1
    return -1


def solution(board):
    row = len(board)
    col = len(board[1])
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                return bfs(i, j, row, col, board)