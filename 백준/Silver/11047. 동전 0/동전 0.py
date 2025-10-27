N, target = map(int,input().split())
coins = [int(input()) for _ in range(N)]
answer = 0

coins.sort(reverse = True)
# 이거 무슨 대표문제인데.. 그리디였나?
# 특정 단위에서 나눠지면 해당 나머지로
for c in coins:
    if target // c > 0:
        answer += target // c
        target = target % c
print(answer)