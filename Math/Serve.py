
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    total = int(arr[i][0])+int(arr[i][1])+1
    games = (total//2)
    if total % 2 != 0:
        games = games + 1
    if total == 0 or total == 1:
        print("Alice")
    else:
        if games % 2 != 0:
            print("Alice")
        else:
            print("Bob")
