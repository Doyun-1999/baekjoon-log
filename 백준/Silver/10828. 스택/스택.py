import sys
input = sys.stdin.readline

N = int(input())
arr = []
            
def push(arr, num):
    arr.append(num)

def pop(arr):
    if not arr:
        print(-1)
    else:
        print(arr.pop(len(arr)-1))

def size(arr):
    print(len(arr))

def empty(arr):
    if not arr:
        print(1)
    else:
        print(0)

def top(arr):
    if not arr:
        print(-1)
    else:
        print(arr[len(arr) -1])

for _ in range(N):
    command = input().split()
    if command[0] == "push":
        num = command[1]
        push(arr, num)
    elif command[0] == "top":
        top(arr)
    elif command[0] == "size":
        size(arr)
    elif command[0] == "empty":
        empty(arr)
    elif command[0] == "pop":
        pop(arr)