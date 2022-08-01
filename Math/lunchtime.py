# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    if arr[i]>=1 and arr[i]<=4:
        print("YES")
    else:
        print("NO")
