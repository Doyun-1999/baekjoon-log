N = int(input())
dic = set()

for i in range(N):
    dic.add(input())

sorted_dic = sorted(dic, key=lambda x: (len(x), x))

for word in sorted_dic:
    print(word)