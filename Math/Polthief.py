# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    distance = int(arr[i][1])-int(arr[i][0])
    if distance<0:
        distance = distance*(-1)
    print(distance)
