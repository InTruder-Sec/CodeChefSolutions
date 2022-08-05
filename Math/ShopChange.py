# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    arr.append(m)
for i in range(t):
    back = 100 - int(arr[i])
    print(back)
