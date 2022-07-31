# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    vol = int(arr[i][1])-int(arr[i][0])
    if vol<1:
        vol = vol*(-1)
    print(vol)
