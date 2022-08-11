# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    n = int(arr[i][0])
    x = int(arr[i][1])
    k = int(arr[i][2])
    total = k//x
    if total>n:
        print(n)
    else:
        print(total)
