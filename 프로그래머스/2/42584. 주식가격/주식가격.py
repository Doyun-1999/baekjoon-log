# 우선! prices의 길이만큼의 [0] * len(prices)인 배열을 선언
# 해당 배열은 prices와 인덱스를 공유하며, 더 큰 수가 나올때까지 += 1 을 한다.
def solution(prices):
    l = len(prices)
    tmp = [0] * l
    for i in range(l):
        for j in range(i+1,l):
            if prices[i] <= prices[j]:
                tmp[i] += 1
            else:
                tmp[i] += 1
                break
    return tmp