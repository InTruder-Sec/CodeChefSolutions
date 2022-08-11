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
    sum = a + b
    rem = 21 - sum
    if rem>10 or rem<1 :
        print("-1")
    else: 
        print(rem)
        
