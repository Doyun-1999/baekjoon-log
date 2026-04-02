## 우선 phone_book을 순회하면서 찾아야겠다.
## 2중 포문으로 순회하면서 하나씩 startswith()를 사용하다가 접두어 만나면 탈출? -> 시간초과날듯 O(N^2)
## 문제가 해시로 풀라고했으니까 그걸생각해보자.

def solution(phone_book):
    
    s = set(phone_book)
    
    for book in s:
        p = ""
        for i in range(len(book)-1):
            p += book[i]
            if p in s:
                return False
    return True