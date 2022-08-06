# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = int(input())
    arr.append(m)
for i in range(t):
    cars = arr[i]//4
    if arr[i]%4!=0:
        cars = cars + 1
    print(cars)
