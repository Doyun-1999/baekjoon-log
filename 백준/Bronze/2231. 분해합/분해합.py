n = int(input())
i = 1

while i < n:
    lst = []
    for j in str(i):
        lst.append(int(j))
        
    s = sum(lst)
    if n == i + s:
        print(i)
        break
    i += 1
else:
    print(0)
