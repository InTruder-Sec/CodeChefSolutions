# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    points = int(arr[i][1]) + int(arr[i][2])*2
    if int(arr[i][0])>points:
        print("NotQualify")
    else:
        print("Qualify")
