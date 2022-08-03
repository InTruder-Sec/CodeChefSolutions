# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    left = int(arr[i][1]) - int(arr[i][0])
    total = int(arr[i][2])*int(arr[i][3])
    if total > left:
        print("Overflow")
    elif total < left:
        print("Unfilled")
    else:
        print("Filled")
