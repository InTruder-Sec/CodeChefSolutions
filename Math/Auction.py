# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    a = int(arr[i][0])
    b = int(arr[i][1])
    c = int(arr[i][2])
    if b > a:
        if c>b:
            largest = "Charlie"
        else:
            largest = "Bob"
    else:
        if c>a:
            largest = "Charlie"
        else:
            largest = "Alice"
    print(largest)
