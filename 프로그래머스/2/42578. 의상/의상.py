## 우선 key,value로 묶는 dictionary가 자료구조에서 먼저 떠오른다
## 우선 len(clothes) 는 기본으로 무조건 입는거고
## 추가로 이제 겹쳐입는 경우의 수는 곱셈으로 key의 개수의 곱셈으로
## 최종답은 len(clothes) + key의 개수의 곱
def solution(clothes):
    d = {}
    answer = 1
    
    for c in clothes:
        if c[1] not in d:
            d[c[1]] = []   # 리스트 생성
        d[c[1]].append(c[0])
            
    for v in d.values():
        answer *= (len(v) + 1)
        
    return answer-1