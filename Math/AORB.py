# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    pnt_a = 500 - (int(arr[i][0])*2)
    pnt_b = 1000 - ((int(arr[i][0])+int(arr[i][1]))*4)
    total1 = pnt_b + pnt_a
    pnt_b = 1000 - (int(arr[i][1])*4)
    pnt_a = 500 - ((int(arr[i][0]) + int(arr[i][1]))*2)
    total2 = pnt_a + pnt_b
    if total1>total2:
        print(total1)
    else:
        print(total2)
    
