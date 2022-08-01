# cook your dish he
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)

for i in range(t):
    # 1st sum
    sum1 = int(arr[i][0]) + int(arr[i][1])
    sum2 = int(arr[i][2]) + int(arr[i][3])
    if sum1 > sum2:
        print(sum2)
    else:
        print(sum1)
