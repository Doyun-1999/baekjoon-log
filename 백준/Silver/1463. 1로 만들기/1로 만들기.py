# 나누어서 1만드는 최소 연산 개수를 구하자 -> 그리디 냄새남 동전만들기?
# 1번 아이디어 - 최대한 3으로나누고 최대한 2로나누고 -1을 한다? 그것도 아님
# 2번 아이디어 - 나눠서 나머지가 1이면 -1하고 3으로나누기 -> 나눠서 나머지가 2이면 2로그냥 나누기! 하면될거같음
N = int(input())
cnt = 0

dp = [0] * (N+1)
dp[1] = 0
for x in range(2,N+1):
    best = dp[x-1]
    if x%2 == 0:
        best = min(best, dp[x//2])
    if x%3 == 0:
        best = min(best, dp[x//3])
    dp[x] = 1 + best
    
print(dp[N])