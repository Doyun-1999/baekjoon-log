N, K = map(int,input().split())
t = []
for i in range(N):
    t.append(list(map(int,input().split()))) # [무게,가치]
    
dp = [0] * (K+1) # 최대 가치를 저장하는 dp 테이블

for w, v in t:  # w: 무게, v: 가치
    for i in range(K, w - 1, -1):  # 역순으로 갱신
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])