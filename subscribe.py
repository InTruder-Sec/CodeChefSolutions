# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m =int(input())
    arr.append(m)
for i in range(t):
    if int(arr[i])>30:
        print("YES")
    else:
        print("NO")
