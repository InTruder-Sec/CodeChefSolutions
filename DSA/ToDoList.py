# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    rate = input()
    rate = rate.split()
    arr.append(rate)
for i in range(t):
    rem = 0
    for q in range(len(arr[i])):
        if int(arr[i][q])>=1000:
            rem = rem + 1
    print(rem)
