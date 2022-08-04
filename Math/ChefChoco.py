# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    left = int(arr[i][0]) - int(arr[i][1])
    price = left*int(arr[i][2])
    if left<0:
        price = 0
    print(price)
