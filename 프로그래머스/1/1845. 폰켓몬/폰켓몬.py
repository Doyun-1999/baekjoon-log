def solution(nums):
    s = set()
    m = len(nums)//2
    
    for n in nums:
        s.add(n)
    
    if m <= len(s) :
        return m
    else:
        return len(s)