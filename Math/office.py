t = int(input())
arr=[]
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    week_days = int(arr[i][0])*4
    week_end = int(arr[i][1])
    total_hours = week_end + week_days
    print(total_hours)
