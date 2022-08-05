# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    money = int(arr[i][0])*10 + int(arr[i][1])*5
    print(money)
