def solution(clothes):
    hashmap = {}
    for cloth, category in clothes:
        if category not in hashmap:
            hashmap[category] = []
        hashmap[category].append(cloth)
    
    answer = 1
    for category in hashmap:
        answer *= (len(hashmap[category]) + 1)  # 입거나 안 입거나
    
    return answer - 1  # 아무것도 안 입는 경우 제외
