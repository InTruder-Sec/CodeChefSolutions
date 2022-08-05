# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m =input()
    arr.append(m)
for i in range(t):
    time = int(arr[i]) + 3
    if time>10:
        print("NO")
    else:
        print("YES")
