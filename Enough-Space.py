# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    req = (int(arr[i][1]) + (int(arr[i][2])*2))
    dif = int(arr[i][0]) - int(req)
    if dif < 0:
        print("NO")
    else:
        print("YES")
