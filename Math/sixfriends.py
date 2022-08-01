# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    cost1 = int(arr[i][0])*3
    cost2 = int(arr[i][1])*2
    if cost2>=cost1:
        print(cost1)
    else:
        print(cost2)
