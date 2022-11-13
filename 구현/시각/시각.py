import sys ; sys.stdin = open("시각.txt")

N = int(input())

# 60초 = 1분
# 60분 = 1시간
# 시간이 N이 되기 전까지 계속 구해봅니다.
answer = 0
for hour in range(N+1):
    for minutes in range(60):
        for seconds in range(60):
            if '3' in str(hour) + str(minutes) + str(seconds):
                answer += 1

print(answer)