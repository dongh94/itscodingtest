import sys; sys.stdin = open("큰수의법칙.txt")
n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
while 0 <= m:
    for i in range(k):
        if m == 0: break;
        result += first
        m -= 1
    if m == 0: break;
    result += second
    m -= 1

print(result)
