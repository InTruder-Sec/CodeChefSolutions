# cook your dish here
t = int(input())
arr =[]
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total = int(arr[i][0]) + int(arr[i][1]) + int(arr[i][2])
    if total>=100 and (int(arr[i][0])>=10 and int(arr[i][1])>=10 and int(arr[i][2])>=10):
        print("PASS")
    else:
        print("FAIL")
