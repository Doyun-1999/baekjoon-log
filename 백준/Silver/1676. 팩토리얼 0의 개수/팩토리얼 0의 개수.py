N = int(input())
factorial = 1
lst = []
cnt = 0

for i in range(1,N+1):
    factorial = factorial*i

s_factorial = str(factorial) 

for j in s_factorial[::-1]:
    if j == '0':
        cnt += 1
    else:
        break  # 0이 아닌 숫자가 나오면 즉시 종료

print(cnt)