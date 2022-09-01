import sys; sys.stdin = open("greed_숫자카드게임.txt")
n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_v = min(arr)
    result = max(result, min_v)

print(result)


