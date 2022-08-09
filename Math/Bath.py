# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    one_p = int(arr[i][1])*2
    total = int(arr[i][0])//one_p
    print(total)
