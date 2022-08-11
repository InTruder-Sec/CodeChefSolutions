# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    if arr[i]<=15:
        print("yes")
    else:
        print("NO")
