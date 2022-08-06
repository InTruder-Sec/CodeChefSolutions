# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    val1 = False
    val2 = False
    if int(arr[i][1])>=int(arr[i][0]):
        val1 = True
    if int(arr[i][1])%int(arr[i][0])==0:
        val2 = True
    if val1 == True and val2 == True:
        print("YES")
    else:
        print("NO")
