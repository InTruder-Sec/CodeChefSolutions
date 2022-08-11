# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    dif = int(arr[i][1])-int(arr[i][0])
    if dif%8!=0:
        num = (dif//8)+1
    else:
        num = dif//8
    print(num)
