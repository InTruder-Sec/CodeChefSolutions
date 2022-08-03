# cook your dish here
t = int(input())
arr  = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total = int(arr[i][1])*30
    if total>int(arr[i][0]):
        print("NO")
    else:
        print("YES")
