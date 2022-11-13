import sys; sys.stdin=open("1이될때까지.txt")
tc = 2
for _ in range(tc):
    n, k = map(int,input().split())
    answer = 0
    while n > 1:
        while not n % k:
            n //= k
            answer += 1
        if n == 1: break;
        n -= 1
        answer += 1
    print(answer)

