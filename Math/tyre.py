# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total = int(arr[i][0])*2 + int(arr[i][1])*4
    print(total)
