# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    score_test = int(arr[i][0])/10
    total_score = int(score_test)*(int(arr[i][1]))
    print(total_score)
