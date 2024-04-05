from collections import deque

def print_arr(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i == len(arr)-1:
            print(arr[i], end="")
            break
        print(arr[i], end=",")
    print("]", end="")
    print()

t = int(input())
for _ in range(t):
    p = deque(list(input()))
    n = int(input())

    arr = deque(list(input().lstrip("[").rstrip("]").split(",")))
    if n == 0:
        arr = []

    flag = True
    printable = True
    while p:
        func = p.popleft()
        if func == "R":
            flag = not flag
        else:
            if len(arr) == 0:
                print("error")
                printable = not printable
                break
            if flag:
                arr.popleft()
            else:
                arr.pop()

    if printable and flag:
        print_arr(list(arr))
    elif printable and not flag:
        print_arr(list(arr)[::-1])