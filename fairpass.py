# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)

for i in range(t):
    if int(arr[i][0]) < int(arr[i][1]):
        print("Yes")
    elif int(arr[i][0]) > int(arr[i][1]):
        print("No")
