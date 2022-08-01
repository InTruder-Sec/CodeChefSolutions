# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    arr.append(m)
for i in range(t):
    coins  = int(arr[i])%10
    print(coins)
