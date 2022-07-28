# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)

for i in range(t):
    sum = []
    first = int(arr[i][0]) + int(arr[i][2]) #A AND C
    sum.append(first)
    second = int(arr[i][0]) + int(arr[i][3]) #A AND D
    sum.append(second)
    third = int(arr[i][1]) + int(arr[i][2]) #B AND C
    sum.append(third)
    fourth = int(arr[i][1]) + int(arr[i][3]) #B AND D
    sum.append(fourth)
    max_no = max(sum)
    print(max_no)
