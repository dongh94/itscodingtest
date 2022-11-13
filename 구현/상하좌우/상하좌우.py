import sys; sys.stdin=open("상하좌우.txt")

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
                print("경로를 이탈")
                break;
        r, c = nr, nc
print('마지막 좌표는 :','(',r+1,',',c+1,')')
print(f'마지막 좌표는 : ( {r+1} , {c+1} )')
