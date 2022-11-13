import sys; sys.stdin=open("implemented_상하좌우.txt")

#N 입력받고
n = int(input())

#방향

move = ['U','D','L','R']
dr = [-1,1,0,0]
dc = [0,0,-1,1]
r = c = 0
move_input = list((input().split()))
for m in move_input:
    nr, nc = r, c
    for d in range(4):
        if m == move[d]:
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 > nr or nr >= n or 0 > nc or nc >= n:
                break
        r, c = nr, nc
print(r+1, c+1)
