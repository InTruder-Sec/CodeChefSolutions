# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    tile = 0
    if int(arr[i][0])%2!=0:
        tile = tile + int(arr[i][1])
    if int(arr[i][1])%2!=0:
        tile = tile + int(arr[i][0])
    if int(arr[i][0])%2!=0 and int(arr[i][1])%2!=0:
        tile = tile-1
    print(tile)
