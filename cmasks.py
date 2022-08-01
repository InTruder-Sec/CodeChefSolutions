# cook your dish here
t=int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    dis = int(arr[i][0])*100
    clo = int(arr[i][1])*10
    if clo <= dis:
        print("Cloth")
    else:
        print("Disposable")
