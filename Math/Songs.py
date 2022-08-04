# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    n = 0
    for t in range(1, int(arr[i][0])+1):
        k = int(arr[i][1])
        if t%(k*3)==0:
            n = n+1
    print(n)
