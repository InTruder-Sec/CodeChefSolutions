# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    arr.append(m)
for i in range(t):
    disc = int(arr[i])*0.1
    disc2 = 100
    if disc2>disc:
        print(int(disc2))
    else:
        print(int(disc))
