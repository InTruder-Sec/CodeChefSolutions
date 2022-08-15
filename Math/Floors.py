# cook your dish here
t = int(input())
arr = []
for i in range(t):
    m = input()
    m = m.split()
    arr.append(m)
for i in range(t):
    t = 0 
    while True:
        c_f = int(arr[i][0])+t
        t = t + 1
        if c_f%10==0:
            c_f = c_f//10
            t = 0
            break
    while True:
        cn_f = int(arr[i][1]) + t
        t = t + 1
        if cn_f%10==0:
            cn_f = cn_f//10
            t = 0
            break
    diff = cn_f - c_f
    if diff<0:
        diff = diff*(-1)
    print(diff)
        
        
