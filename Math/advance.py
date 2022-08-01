# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    score = int(arr[i][0]) + 200
    if int(arr[i][1])<=int(score) and int(arr[i][0])<=int(arr[i][1]):
        print("YES")
    else:
        print("NO")
