# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    max_time = (int(arr[i][0])*0.07)+int(arr[i][0])
    if int(arr[i][1])>max_time:
        print("No")
    else:
        print("Yes")
