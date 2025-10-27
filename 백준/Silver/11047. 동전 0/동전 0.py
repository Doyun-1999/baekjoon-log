N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse = True)

answer = 0
for c in coins:
    if K // c > 0:
        answer += K // c
        K = K % c
        
print(answer)