# 두개의 합이 가장 0에 가까운 경우니까 투포인터로 합의 절대값이 가장 작은거..? 찾아야겠지?
# 파이썬에서 절대값 함수를 모르니까 조건문으로 풀어가보자~~

N = int(input())
liquid = list(map(int,input().split()))
liquid.sort() # liquid 배열 정렬

s,e = 0, N-1 # s는 시작 e는 마지막 인덱스 지정
p = 0 # 두 용액의 합을 저장하는 변수
answer = (liquid[s],liquid[e]) # 초기값 설정

while s<e:
    p = liquid[s] + liquid[e]
    if abs(p) < abs(sum(answer)):
        answer = (liquid[s], liquid[e])
        
    if p < 0:
        s += 1
    elif p > 0:
        e -= 1
    else:
        answer = (liquid[s], liquid[e])
        break
print(answer[0], answer[1])