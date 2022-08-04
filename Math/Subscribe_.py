# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    sub = int(arr[i][0])//6
    if int(arr[i][0])%6!=0:
        sub = sub + 1
    cost = sub*int(arr[i][1])
    print(cost)
