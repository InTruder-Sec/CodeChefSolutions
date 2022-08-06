# cook your dish here
t = int(input())
arr =[]
for i in range(t):
    m =input()
    m = m.split()
    arr.append(m)
for i in range(t):
    rem = int(arr[i][0]) - int(arr[i][1])
    t = rem//4
    if rem%4!=0:
        t = t + 1
    if t<0:
        t = 0
    print(t)
    
