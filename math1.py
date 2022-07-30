# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    dif = int(arr[i][1]) - int(arr[i][0])
    if dif <=0:
        print("0")
    else:
        print(dif)
