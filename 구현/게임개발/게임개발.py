import sys; sys.stdin = open('게임개발.txt')

N, M = map(int, input().split())
A, B, d = map(int,input().split())
arr = [[-1]*(N+1)] + [[-1] + list(map(int,input().split())) for _ in range(N)]
# 상 우 하 좌
# 좌 상 우 하
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
op = [2, 3, 0, 1]
visited = [[0]*(N+1) for _ in range(N+1)]
# 첫 위치, 첫 방향은 d
r = A
c = B
while True:
    cnt = 0
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 1 or nr > N+1 or nc < 1 or nc > M+1:
            cnt += 1
            continue

        if visited[nr][nc] or arr[nr][nc] == 1:
            cnt += 1
            continue

        if not visited[nr][nc] and arr[nr][nc] == 0:
            visited[nr][nc] = 1
            r, c = nr, nc
            break






