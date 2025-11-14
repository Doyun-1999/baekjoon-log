# 투포인터 슬라이딩 윈도우
# 누적합을 저장하면서 target 보다 작다면?
N, target = map(int,input().split())
numbers = list(map(int,input().split()))

s,e = 0,0
m = [] # 가장 짧은 길이 저장하는 변수 (길이는 e-s+1)
total = numbers[0] # 누적합 저장
answer = 0

while True:
    if total<target: # 누적합<타겟 넘버
        e+=1
        if e == N:
            break
        total += numbers[e]
    elif total>=target:
        m.append(e-s+1)
        total -= numbers[s]
        s+=1
    
if len(m) != 0:
    answer = min(m)
else:
    answer = 0
print(answer)