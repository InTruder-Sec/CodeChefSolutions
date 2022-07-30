# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    diff1 = 7 - int(arr[i][0])
    diff2 = 7 - int(arr[i][1])
    if diff2>=diff1:
        print(diff1)
    else:
        print(diff2)
