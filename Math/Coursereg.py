# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    cap = int(arr[i][1]) - int(arr[i][2])
    if cap < int(arr[i][0]):
        print("NO")
    else:
        print("YES")
