# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    arr.append(m)
for i in range(t):
    min = int(arr[i])*60
    game = min//20
    print(game)
