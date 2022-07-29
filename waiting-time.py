# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total_days = int(arr[i][0])*7
    dif = total_days - int(arr[i][1])
    print(dif)
