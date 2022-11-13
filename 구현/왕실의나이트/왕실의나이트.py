import sys; sys.stdin = open("왕실의나이트.txt")

S = input()
r = int(S[1])
# java에서도 사용되는데 암묵적 형변환으로서 int가 아닐때 int로 만드는 방법이다.
c = ord(S[0]) - ord('a') + 1
# 이동 경로 위치 (행/열)
# 총 8방향 (상상좌, 상상우, 우우상, 우우하, 하하좌, 하하우, 좌좌상, 좌좌하)
dr = [-2, -2, -1, 1, 2, 2, -1, 1]
dc = [-1, 1, 2, 2, -1, 1, -2, -2]
answer = 0
for d in range(8):
    nr = r + dr[d]
    nc = c + dc[d]
    if nr < 1 or nr > 8 or nc < 1 or nc > 8: continue;
    answer += 1
print(answer)
