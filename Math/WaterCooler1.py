# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    rent = int(arr[i][0])*int(arr[i][2])
    pur = int(arr[i][1])
    if rent<pur:
        print("YES")
    else:
        print("NO")
