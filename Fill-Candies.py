t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total_space = int(arr[i][1])*int(arr[i][2])
    bag_req = int(arr[i][0])//int(total_space)
    if int(arr[i][0])%int(total_space) != 0:
        bag_req = bag_req + 1 
    print(bag_req)
