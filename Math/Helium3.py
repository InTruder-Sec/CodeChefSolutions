# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total_p = int(arr[i][2])*int(arr[i][3])
    total_r = int(arr[i][0])*int(arr[i][1])
    if total_r>total_p:
        print("NO")
    else:
        print('YES')
