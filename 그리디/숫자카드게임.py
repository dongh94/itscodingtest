import sys; sys.stdin = open("숫자카드게임.txt")

tc = int(input())
for t in range(tc):

    n, m = map(int, input().split())
    max_v = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        min_v = min(arr)
        max_v = max(max_v, min_v)

    print(max_v)


