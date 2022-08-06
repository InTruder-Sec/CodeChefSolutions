# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    val1 = int(arr[i][0])*10
    val2 = int(arr[i][1])*5
    if val1>val2:
        print("FIRST")
    elif val1< val2:
        print("SECOND")
    else:
        print('ANY')
