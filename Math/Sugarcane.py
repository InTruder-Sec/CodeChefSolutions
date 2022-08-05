# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    income = arr[i]*50
    profit = income*0.3
    print(int(profit))
