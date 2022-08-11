# cook your dish here
arr = input()
arr = arr.split()
t = 0
lenn = len(arr)
for i in range(lenn):
    if int(arr[i])>=10:
        t = t + 1
print(t)
