# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    bits = int(arr[i])
    if bits%4==0:
        print("GOOD")
    else:
        print("NOT GOOD")
