# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    level_time = int(arr[i][0])*int(arr[i][1])
    #extra break time 
    no_of_breaks = int(arr[i][0])//3
    if int(arr[i][0])%3==0:
        no_of_breaks = no_of_breaks - 1
    extra_time = no_of_breaks*int(arr[i][2])
    total_time = int(level_time) + int(extra_time)
    print(total_time)
