import sys; sys.stdin=open("greed_1이될때까지.txt")

n, k = map(int,input().split())
result = 0
while n > 1:
    while not n % k:
        n //= k
        result += 1
    if n == 1: break;
    n -= 1
    result += 1
print(result)

