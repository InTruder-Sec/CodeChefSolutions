t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for k in range(t):
    if int(arr[k][1])>int(arr[k][0]):
        print(arr[k][0])
    else:
        print(arr[k][1])
