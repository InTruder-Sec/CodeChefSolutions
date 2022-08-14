# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    if arr[i]%5==0:
        ten = arr[i]//10
        rem = arr[i]%10
        five = rem//5
        total = ten + five
        print(total)
    else:
        print("-1")
