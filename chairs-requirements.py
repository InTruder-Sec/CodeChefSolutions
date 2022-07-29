# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    chairs = int(arr[i][0]) - int(arr[i][1])
    if chairs<0:
        print("0")
    else:
        print(chairs)
