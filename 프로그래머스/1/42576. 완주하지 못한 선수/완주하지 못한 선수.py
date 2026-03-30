def solution(participant, completion):
    
    d = {}
    
    for p in participant:
        d[p] = d.get(p, 0) + 1
        
    for c in completion:
        d[c] -= 1
    
    for key,value in d.items():
        if value == 1:
            return key