# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    x = int(arr[i][0])
    y = int(arr[i][1])
    a = int(arr[i][2])
    if a>=x and a<y:
        print("YES")
    else:
        print("NO")
